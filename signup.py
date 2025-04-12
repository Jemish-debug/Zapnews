import mysql.connector
import re
import random
from sendEmail import send_email

# Temporary OTP store
otp_store = {}

def signupAuthentication(name, email, password, entered_otp=None):
    # Input validation
    if not name or not email or not password:
        return "Signup not successful: All fields are required."

    # Email format check
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        return "Signup not successful: Invalid email format."

    if len(password) < 8 or ' ' in password:
        return "Signup not successful: Password must be at least 8 characters long and have no spaces."

    # Check if OTP needs to be verified
    if entered_otp is not None:
        if email not in otp_store:
            return "Signup not successful: OTP not sent or expired."
        if otp_store[email] != entered_otp:
            return "Signup not successful: Incorrect OTP."

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zapnews"
        )
        print("Database connected successfully!")
        cur = con.cursor()

        sql = "INSERT INTO signup(name, email, password) VALUES (%s, %s, %s)"
        val = (name, email, password)

        cur.execute(sql, val)
        con.commit()

        if email in otp_store:
            otp_store.pop(email)  # clear OTP once used

        return "Signup is successful"

    except mysql.connector.IntegrityError as e:
        if "Duplicate entry" in str(e):
            return "Signup not successful: Email already exists"
        return f"Signup not successful: {str(e)}"

    except Exception as e:
        return f"Signup not successful: {str(e)}"

    finally:
        if con.is_connected():
            con.close()

def generate_and_send_otp(name, email):
    otp = str(random.randint(100000, 999999))
    otp_store[email] = otp
    subject = "ZapNews Signup OTP Verification"
    body = f"Hello {name},\n\nYour OTP for ZapNews signup is: {otp}\n\nPlease enter this code to complete your signup."
    send_email("your_email@gmail.com", "your_app_password", email, subject, body)
    print(f"OTP sent to {email}: {otp}")
    return "OTP sent to your email."

def otp_pending(email):
    return email in otp_store