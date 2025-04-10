import mysql.connector
import re

def loginAuthentication(email, password):
    # Input validation
    if not email or not password:
        return "Login not successful: All fields are required."

    # Email format check
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        return "Login not successful: Invalid email format."

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zapnews"
        )
        print("Database connected successfully!")

        cur = con.cursor()

        # Parameterized query (safer)
        sql = "SELECT * FROM signup WHERE emailId = %s AND password = %s"
        val = (email, password)
        cur.execute(sql, val)

        result = cur.fetchall()

        if result:
            return "Login is successful"
        else:
            return "Login not successful: Invalid credentials"

    except:
        return "Login not successful: Database error"
    finally:
        if con.is_connected():
            con.close()
