from __future__ import annotations

import html
import os
import re
import sqlite3
from datetime import datetime
from typing import Dict, List

from flask import (
    Flask,
    Response,
    jsonify,
    redirect,
    render_template_string,
    request,
    session,
)


APP_SECRET = os.environ.get("PR10_SECRET", "lab-secret-change-me")
DB_PATH = os.path.join(os.path.dirname(__file__), "pr10_lab.db")

app = Flask(__name__)
app.config["SECRET_KEY"] = APP_SECRET


HOME_TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>PR10 Security Lab (Safe)</title>
</head>
<body>
  <h1>PR10 Security Lab (Safe)</h1>
  <p>This lab demonstrates defensive controls only.</p>

  <h2>Search (Reflected Output with Escaping)</h2>
  <form method="get" action="/search">
    <input type="text" name="q" placeholder="Search text" />
    <button type="submit">Search</button>
  </form>

  <h2>Post Comment (Stored Output with Escaping)</h2>
  <form method="post" action="/comment">
    <input type="text" name="author" placeholder="Author" />
    <input type="text" name="comment" placeholder="Comment" />
    <button type="submit">Post</button>
  </form>

  <h2>Login (Parameterized SQL)</h2>
  <form method="post" action="/login">
    <input type="text" name="username" placeholder="Username" />
    <input type="password" name="password" placeholder="Password" />
    <button type="submit">Login</button>
  </form>

  <p><a href="/comments">View Comments</a></p>
  <p><a href="/profile">View Profile JSON</a></p>
  <p><a href="/security-report">Run Security Self-Check</a></p>
</body>
</html>
"""


def db_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = db_conn()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT DEFAULT ''
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            comment TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )

    # Seed one lab user for login demo.
    cur.execute(
        "INSERT OR IGNORE INTO users(username, password, email) VALUES (?, ?, ?)",
        ("alice", "alice123", "alice@example.local"),
    )

    conn.commit()
    conn.close()


SUSPICIOUS_PATTERNS: Dict[str, re.Pattern[str]] = {
    "xss_script_tag": re.compile(r"<\s*script", re.IGNORECASE),
    "xss_event_handler": re.compile(r"on[a-z]+\s*=", re.IGNORECASE),
    "xss_js_proto": re.compile(r"javascript\s*:", re.IGNORECASE),
    "sqli_union": re.compile(r"\bunion\b\s+\bselect\b", re.IGNORECASE),
    "sqli_boolean": re.compile(r"\bor\b\s+\d+\s*=\s*\d+", re.IGNORECASE),
    "sqli_comment": re.compile(r"(--|/\*)", re.IGNORECASE),
    "sqli_stacked": re.compile(r";\s*\w+", re.IGNORECASE),
}


def security_scan_text(value: str) -> List[str]:
    findings: List[str] = []
    if not value:
        return findings

    for name, pattern in SUSPICIOUS_PATTERNS.items():
        if pattern.search(value):
            findings.append(name)
    return findings


def reject_if_suspicious(value: str, context: str) -> Response | None:
    findings = security_scan_text(value)
    if findings:
        return (
            jsonify(
                {
                    "status": "blocked",
                    "context": context,
                    "reason": "suspicious input pattern detected",
                    "findings": findings,
                }
            ),
            400,
        )
    return None


@app.after_request
def add_security_headers(resp: Response) -> Response:
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Referrer-Policy"] = "no-referrer"
    resp.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
    )
    return resp


@app.route("/")
def home() -> str:
    return HOME_TEMPLATE


@app.route("/search")
def search() -> Response | str:
    q = request.args.get("q", "")
    blocked = reject_if_suspicious(q, "reflected_xss_or_sqli_probe")
    if blocked:
        return blocked

    # Escaped output prevents reflected XSS.
    safe_q = html.escape(q)
    return f"<h2>Search Result</h2><p>You searched: {safe_q}</p><p><a href='/'>Back</a></p>"


@app.route("/comment", methods=["POST"])
def post_comment() -> Response:
    author = request.form.get("author", "").strip()
    comment = request.form.get("comment", "").strip()

    blocked_a = reject_if_suspicious(author, "stored_xss_author")
    if blocked_a:
        return blocked_a

    blocked_c = reject_if_suspicious(comment, "stored_xss_comment")
    if blocked_c:
        return blocked_c

    if not author or not comment:
        return (
            jsonify({"status": "error", "message": "author and comment required"}),
            400,
        )

    # Store escaped content to reduce stored XSS risk.
    safe_author = html.escape(author)
    safe_comment = html.escape(comment)

    conn = db_conn()
    conn.execute(
        "INSERT INTO comments(author, comment, created_at) VALUES (?, ?, ?)",
        (safe_author, safe_comment, datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()

    return redirect("/comments")


@app.route("/comments")
def comments() -> str:
    conn = db_conn()
    rows = conn.execute(
        "SELECT author, comment, created_at FROM comments ORDER BY id DESC"
    ).fetchall()
    conn.close()

    items = "".join(
        f"<li><b>{row['author']}</b>: {row['comment']} <small>({row['created_at']})</small></li>"
        for row in rows
    )
    return f"<h2>Comments</h2><ul>{items}</ul><p><a href='/'>Back</a></p>"


@app.route("/login", methods=["POST"])
def login() -> Response:
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    blocked_u = reject_if_suspicious(username, "login_username")
    if blocked_u:
        return blocked_u

    blocked_p = reject_if_suspicious(password, "login_password")
    if blocked_p:
        return blocked_p

    conn = db_conn()
    row = conn.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, password),
    ).fetchone()
    conn.close()

    if row is None:
        return jsonify({"status": "denied", "message": "invalid credentials"}), 401

    session["user"] = row["username"]
    session["csrf"] = secrets_token()
    return jsonify({"status": "ok", "message": f"welcome {row['username']}"})


def secrets_token() -> str:
    return os.urandom(16).hex()


@app.route("/profile")
def profile() -> Response:
    # JSON response avoids direct HTML/JS context injection.
    user = session.get("user", "guest")
    return jsonify(
        {
            "user": user,
            "note": "Render with safe DOM APIs on client (textContent, not innerHTML).",
        }
    )


@app.route("/account/update-email", methods=["POST"])
def update_email() -> Response:
    user = session.get("user")
    csrf = session.get("csrf")
    sent_csrf = request.form.get("csrf", "")
    email = request.form.get("email", "")

    if not user:
        return jsonify({"status": "error", "message": "login required"}), 401
    if not csrf or sent_csrf != csrf:
        return jsonify({"status": "error", "message": "invalid csrf token"}), 403

    blocked = reject_if_suspicious(email, "update_email")
    if blocked:
        return blocked

    conn = db_conn()
    conn.execute("UPDATE users SET email = ? WHERE username = ?", (email, user))
    conn.commit()
    conn.close()

    return jsonify({"status": "ok", "message": "email updated"})


@app.route("/account/delete", methods=["POST"])
def delete_account() -> Response:
    user = session.get("user")
    csrf = session.get("csrf")
    sent_csrf = request.form.get("csrf", "")

    if not user:
        return jsonify({"status": "error", "message": "login required"}), 401
    if not csrf or sent_csrf != csrf:
        return jsonify({"status": "error", "message": "invalid csrf token"}), 403

    conn = db_conn()
    conn.execute("DELETE FROM users WHERE username = ?", (user,))
    conn.commit()
    conn.close()

    session.clear()
    return jsonify({"status": "ok", "message": "account deleted"})


@app.route("/security-report")
def security_report() -> Response:
    """
    Defensive analysis summary for requested classes.
    """
    report = {
        "xss": {
            "reflected_non_persistent": "Escaping output + input scan",
            "stored_persistent": "Escaping before store + output-safe rendering",
            "dom_based": "Serve JSON and recommend safe DOM APIs",
            "javascript_context": "CSP script-src self and no inline script sinks",
        },
        "sql_injection": {
            "union_based": "Parameterized queries + suspicious pattern blocking",
            "error_based": "Generic JSON errors; no SQL error leakage",
            "boolean_blind": "Parameterized queries remove expression injection",
            "login_bypass": "Parameterized auth query",
            "update_delete_tampering": "Parameterized UPDATE/DELETE + session/CSRF checks",
            "stacked_queries": "No dynamic SQL concatenation; execute with placeholders",
        },
    }
    return jsonify(report)


def main() -> None:
    init_db()
    print("PR10 Safe Lab server starting on http://127.0.0.1:5010")
    print("Open /security-report for defensive analysis summary.")
    app.run(host="127.0.0.1", port=5010, debug=False)


if __name__ == "__main__":
    main()
