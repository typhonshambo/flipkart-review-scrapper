from flask import Flask, render_template, request
from scrapper import scraper
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    scraper(keyword)  # Perform scraping for the provided keyword
    with open("data.json", "r") as f:
        data = json.load(f)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
