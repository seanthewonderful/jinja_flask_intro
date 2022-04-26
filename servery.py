from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    rand_num = random.randint(1,10)
    current_year = datetime.datetime.today().year
    return render_template("index.html", num=rand_num, current_year=current_year)


@app.route('/guess/<name>')
def guess(name):
    data = requests.get("https://api.agify.io?name=" + name).json()
    g_data = requests.get("https://api.genderize.io?name=" + name).json()
    gender = g_data["gender"]
    age = data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
    
    

if __name__ == "__main__":
    app.run(debug=True)