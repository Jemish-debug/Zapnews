import mysql.connector

def signupAuthentication(name, email, password):
    try:
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "zapnews"
        )
        print("Database connected successfully!!!")
        cur = con.cursor()
        sql = "INSERT INTO signup(name, emailId, password) VALUES (%s, %s, %s)"
        val = (name, email, password)
        print(sql)
        cur.execute(sql, val)
        con.commit()
    except:
        print("Connection Error")
    finally:
        con.close()