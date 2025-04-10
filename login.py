import mysql.connector
import re

def loginAuthentication(email, password):
    if not email or not password:
        return "Login not successful: All fields are required.", ""

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        return "Login not successful: Invalid email format.", ""

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zapnews"
        )
        print("Database connected successfully!")
        cur = con.cursor()

        sql = "SELECT name FROM signup WHERE email = %s AND password = %s"
        val = (email, password)
        cur.execute(sql, val)
        result = cur.fetchone()

        if result:
            return "Login is successful", result[0]  # return name as second value
        else:
            return "Login not successful: Invalid credentials", ""
    except:
        return "Login not successful: Database error", ""
    finally:
        if con.is_connected():
            con.close()
            print("Database disconnected")

