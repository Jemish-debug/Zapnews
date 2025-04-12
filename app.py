from flask import Flask, render_template, request, redirect, url_for
import json
import fetch
import login
import signup
import userpreferences
import newsFiltration
import categoryNews
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

fetch.fetchHeadlines()

#<-------------- LOGIN FUNCTION -------------->
@app.route('/', methods=['GET', 'POST'])
def loginValue():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        res, name = login.loginAuthentication(email, password)
        print(f"Login attempt - Email: {email}, Password: {password}")
        print(res)

        if res == "Login is successful":
            return render_template("login.html", message=res, name=name, email=email)
        else:
            return render_template("login.html", message=res)

    return render_template("login.html")
#<------------------------------------------------------>

#<-------------- SIGNUP FUNCTION -------------->
@app.route('/signup', methods=['GET', 'POST'])
def signupValue():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(f"Signup attempt - Name: {name}, Email: {email}, Password: {password}")
        res = signup.signupAuthentication(name, email, password)
        print("Signup: ", res)

        if res == "Signup is successful":
            return render_template("signup.html", message=res, email=email, name=name)
        else:
            return render_template("signup.html", message=res)

    return render_template("signup.html")
#<------------------------------------------------------>

#<-------------- USER PREFERENCE FUNCTION -------------->
@app.route('/preference_filter', methods=['GET', 'POST'])
def userPreference():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        print("DEBUG: Email from form:", email)
        print("DEBUG: Name from form:", name)

        selected = [val for key, val in request.form.items() if key not in ('email', 'name')]
        result = userpreferences.savePreferences(email, selected)
        print("DEBUG: Save result:", result)

        return render_template("preference_filter.html", email=email, name=name, message=result)

    email = request.args.get('email', '')
    name = request.args.get('name', '')
    print("DEBUG: Email from URL:", email)
    print("DEBUG: Name from URL:", name)

    return render_template("preference_filter.html", email=email, name=name)
#<------------------------------------------------------>

@app.route('/preferencedNews')
def preferencedNews():
    try:
        with open("data\\user_preferenced_news.json", "r", encoding="utf-8") as f:
            news_items = json.load(f)
    except Exception as e:
        print("Error loading user_preferenced_news.json:", e)
        news_items = []

    return render_template("preferencedNews.html", news_items=news_items)

#<-------------- HOME FUNCTION -------------->
@app.route('/home')
def home():
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    print("DEBUG: Name =", name, "| Email =", email)

    news_items = newsFiltration.get_filtered_news(email)
    return render_template("index.html", username=name, news_items=news_items)
#<------------------------------------------------------>

#<-------------- READ NEWS FUNCTION -------------->
@app.route('/read-news')
def read_news():
    url = request.args.get('url')

    if not url:
        return "No article URL provided", 400

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        possible_selectors = [
            'article',
            'div.Normal',
            'div.story-content',
            'div._s30J',
        ]

        article_body = None
        for selector in possible_selectors:
            article_body = soup.select_one(selector)
            if article_body:
                break

        content_html = article_body.prettify() if article_body else "<p>Sorry, article content could not be extracted.</p>"
        return render_template("read_news.html", content=content_html, source_url=url)

    except Exception as e:
        print(f"Error loading article: {e}")
        return "Failed to load article", 500
#<------------------------------------------------------>

def load_news_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error reading {filepath}:", e)
        return []

@app.route('/technologyNews')
def technology():
    news_items = load_news_from_file('data\\technology_news.json')
    return render_template('technologyNews.html', category='Technology', news_items=news_items)

@app.route('/politicsNews')
def politics():
    news_items = load_news_from_file('data\\politics_news.json')
    return render_template('politicsNews.html', category='Politics', news_items=news_items)

@app.route('/articlesNews')
def articles():
    news_items = load_news_from_file('data\\articles_news.json')
    return render_template('articlesNews.html', category='Articles', news_items=news_items)

if __name__ == "__main__":
    app.run(debug=True)
