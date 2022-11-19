from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def init():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/index1')
def index():
        url='https://newsapi.org/v2/top-headlines?country=in&apiKey=0b847d15f1ce42c9a341daa9b3369ad4'
        r=requests.get(url).json()
        cases={
        'articles' : r['articles']
            }
        return render_template("index1.html",case= cases)

@app.route('/login')
def login():
    error=1
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/logout')
def logout():
    return render_template('logout.html') 


if __name__ == '__main__':
    app.run(debug=True)
   
