import mysql.connector

def savePreferences(email, selected_categories):
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zapnews"
        )
        print("Database connected successfully!")
        cur = con.cursor()

        for category in selected_categories:
            cur.execute("SELECT id FROM preferences WHERE LOWER(category_name) = %s", (category.lower(),))
            result = cur.fetchone()
            print(f"[DEBUG] Looking up category '{category}' → Result: {result}")
            
            if result:
                preference_id = result[0]
                cur.execute(
                    "INSERT IGNORE INTO user_preferences (emailId, preference_id) VALUES (%s, %s)",
                    (email, preference_id)
                )
                print(f"[DEBUG] Inserted preference {preference_id} for email: {email}")
            else:
                print(f"[WARN] Category '{category}' not found in preferences table.")

        con.commit()
        return "Preferences saved successfully"

    except Exception as e:
        print("Error:", e)
        return "Failed to save preferences"

    finally:
        if con.is_connected():
            con.close()
