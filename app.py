from flask import Flask, render_template, request, redirect, url_for
import json
import fetch
import login
import signup
import userpreferences

app = Flask(__name__)

def load_news_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)[:10]

@app.route('/', methods=['GET', 'POST'])
def loginValue():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        res = login.loginAuthentication(email, password)
        print(f"Login attempt - Email: {email}, Password: {password}")
        print(res)

        if res == "Login is successful":
            return render_template("login.html", message=res)
        else:
            return render_template("login.html", message=res)

    return render_template("login.html")

@app.route('/preference_filter', methods=['GET', 'POST'])
def userPreference():
    if request.method == 'POST':
        # Get name and email from the hidden form inputs
        email = request.form.get('email')
        name = request.form.get('name')
        print("DEBUG: Email from form:", email)
        print("DEBUG: Name from form:", name)

        # Collect selected checkboxes (excluding email and name)
        selected = [
            val for key, val in request.form.items()
            if key not in ('email', 'name')
        ]

        result = userpreferences.savePreferences(email, selected)
        print("DEBUG: Save result:", result)

        # Render the page again to show the success message and allow redirect via JavaScript
        return render_template("preference_filter.html", email=email, name=name, message=result)

    # If it's a GET request, get name and email from the URL query string
    email = request.args.get('email', '')
    name = request.args.get('name', '')
    print("DEBUG: Email from URL:", email)
    print("DEBUG: Name from URL:", name)

    return render_template("preference_filter.html", email=email, name=name)




@app.route('/signup', methods=['GET', 'POST'])
def signupValue():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(f"Signup attempt - Name: {name}, Email: {email}, Password: {password}")
        res = signup.signupAuthentication(name, email, password)
        print("Signup: ", res)

        # Check if signup was successful to decide if redirect or stay
        if res == "Signup is successful":
            return render_template("signup.html", message=res, email=email, name=name)
        else:
            return render_template("signup.html", message=res)

    return render_template("signup.html")

@app.route('/index')
def home():
    news_items = load_news_data()
    name = request.args.get('name', '')
    return render_template("index.html", username=name, news_items=news_items)







fetch.fetchHeadlines()

if __name__ == "__main__":
    app.run(debug=True)
