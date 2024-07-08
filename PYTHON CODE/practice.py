from cryptography.fernet import Fernet
import sqlite3

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

# Initialize the database
def init_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY, site TEXT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Store an encrypted password in the database
def store_password(site, username, password, key):
    encrypted_password = encrypt_password(password, key)
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)",
              (site, username, encrypted_password))
    conn.commit()
    conn.close()

# Retrieve and decrypt a password from the database
def retrieve_password(site, username, key):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT password FROM passwords WHERE site = ? AND username = ?", (site, username))
    result = c.fetchone()
    conn.close()
    if result:
        return decrypt_password(result[0], key)
    return None
