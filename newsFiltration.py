import json
import mysql.connector

def get_filtered_news(email):
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zapnews"
        )
        cur = con.cursor()

        cur.execute("""
            SELECT p.category_name
            FROM user_preferences up
            JOIN preferences p ON up.preference_id = p.id
            WHERE up.emailId = %s
        """, (email,))
        prefs = [row[0].lower() for row in cur.fetchall()]
        print("DEBUG: Preferences for", email, "→", prefs)

        if not prefs:
            return []

        with open("data\\data.json", "r", encoding="utf-8") as f:
            all_news = json.load(f)

        filtered_news = []
        seen_links = set()

        for article in all_news:
            title = article.get('title', '').lower()
            link = article.get('link', '').lower()

            for pref in prefs:
                if pref in title or pref in link:
                    if link not in seen_links:
                        filtered_news.append(article)
                        seen_links.add(link)

        with open("data\\user_preferenced_news.json", "w", encoding="utf-8") as f:
            json.dump(filtered_news, f, indent=4, ensure_ascii=False)

        print(f"Saved {len(filtered_news)} articles to user_preferenced_news.json")

        return filtered_news

    except Exception as e:
        print("Error filtering news:", e)
        return []

    finally:
        if con.is_connected():
            con.close()
