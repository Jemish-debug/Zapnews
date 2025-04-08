from flask import Flask, render_template, request, redirect, url_for
import json
import fetch
import login
import signup



app = Flask(__name__)

def load_news_data():
    with open('data.json', 'r', encoding = 'utf-8') as f:
        return json.load(f)[:10]
    
@app.route('/', methods = ['GET', 'POST'])
def loginValue():
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']
        
        print(f"Login attempt - Email: {email}, Password: {password}")
        res = login.loginAuthentication(email, password)
        print(res)
        
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route('/signup', methods = ['GET', 'POST'])
def signupValue():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        print(f"Signup attempt - Name: {name}, Email: {email}, Password: {password}")
        res = signup.signupAuthentication(name, email, password)
        print("Signup: ", res)

        return redirect(url_for('home'))
    return render_template("signup.html")

@app.route('/index')
def home():
    news_items = load_news_data()
    return render_template("index.html", news_items = news_items)





fetch.fetchHeadlines()
if __name__ == "__main__":
    app.run(debug = True)
