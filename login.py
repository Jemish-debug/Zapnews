import mysql.connector


def loginAuthentication(email, password):
    try:
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "zapnews"
        )
        print("Database connected successfully!!!")
        cur = con.cursor()
        sql = f"SELECT * FROM signup WHERE emailID = '{email}' and password = '{password}'"
        print(sql)
        cur.execute(sql)
        print("haha")
        result = cur.fetchall()
        print("hihi")
        if result:
            return True
        else:
            return False
    except:
        print("Connection Error")
    finally:
        con.close()
