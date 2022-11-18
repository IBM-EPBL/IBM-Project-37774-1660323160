from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url='https://newsapi.org/v2/top-headlines?country=in&apiKey=e7f35f5c970b482f828551bb8ef90f5d'
    r=requests.get(url).json()
    cases={
        'articles' : r['articles']
    }

    return render_template("index.html",case = cases)
@app.route('/login')
def login():
    error=1
    return render_template("login.html")
if __name__ == '__main__':
    app.run(debug=True)
   
