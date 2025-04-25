import pandas as pd
import smtplib
from email.message import EmailMessage
import ssl
import time

CSV_FILE = "companylistfinal.csv"
RESUME_FILE = "resume.pdf"
YOUR_EMAIL = "pharshil748@gmail.com"
APP_PASSWORD = "nwka dvjh hsun fehn"  


def personalize(text, company_name):
    return text.replace("[Company Name]", company_name)


def send_email(to_email, subject, body, attachment_path):
    msg = EmailMessage()
    msg["From"] = YOUR_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach resume
    with open(attachment_path, "rb") as f:
        resume_data = f.read()
        msg.add_attachment(
            resume_data, maintype="application", subtype="pdf", filename="resume.pdf"
        )

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(YOUR_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        print(f"✅ Email sent to: {to_email}")


def main():
    df = pd.read_csv(CSV_FILE)
    template = """
Respected Hiring Manager,

I am writing to express my interest in the summer internship opportunity at [Company Name]. As a B.Tech student in Computer Engineering at CHARUSAT and a current AI minor student at IIT Mandi, I am excited to bring my technical foundation, problem-solving mindset, and hands-on project experience into a dynamic and growth-driven environment.

Throughout my academic journey, I have built and contributed to projects that reflect real-world problem-solving. Most recently, I developed PyLock, a secure desktop password manager featuring custom password reset logic and email-based two-factor authentication, and I also fully built and deployed my portfolio website using React.js, Next.js, and Tailwind CSS. You can check it out at harshilpatel.me.

My proficiency in languages like Python, Java, and C++, combined with experience using tools like TensorFlow, SQLite, allows me to quickly adapt and contribute to diverse technical environments. Beyond programming, I bring a collaborative attitude, a strong willingness to learn, and an eye for secure, scalable solutions.

I am eager to apply my skills and enthusiasm in a real-world setting, contribute meaningfully to your team, and continue growing as a developer. I would welcome the opportunity to discuss how I can support your work and learn from your team this summer.
Thank you for considering my application. I look forward to the opportunity to speak with you further.

Sincerely,  
Harshil Patel
"""

    for _, row in df.iterrows():
        company = row["Company Name"]
        emails = str(row["Email(s)"]).split(",")
        for email in emails:
            email = email.strip()
            if not email or "@" not in email:
                continue
            subject = f"Summer internship opportunity at {company}"
            body = personalize(template, company)
            try:
                send_email(email, subject, body, RESUME_FILE)
                time.sleep(2)
            except Exception as e:
                print(f"❌ Failed to send to {email}: {e}")


if __name__ == "__main__":
    main()
