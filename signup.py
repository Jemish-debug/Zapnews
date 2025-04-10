import mysql.connector
import re

def signupAuthentication(name, email, password):
    # Input validation
    if not name or not email or not password:
        return "Signup not successful: All fields are required."

    # Email format check
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        return "Signup not successful: Invalid email format."

    if len(password) < 8 or ' ' in password:
        return "Signup not successful: Password must be at least 8 characters long and have no spaces."

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
