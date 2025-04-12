import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to secure
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

send_email(
    sender_email="koladiajemish@gmail.com",
    sender_password="cufc scjo owzx brxv",
    receiver_email="manaspathak100@gmail.com",
    subject="Chicken Pox",
    body="Kesa hai?"
)

# send_email(
#     sender_email="koladiajemish@gmail.com",
#     sender_password="cufc scjo owzx brxv",
#     receiver_email="vanshpatelvsp@gmail.com",
#     subject="CRAZY",
#     body="Automation on it's peak"
# )