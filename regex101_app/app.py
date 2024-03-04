# app.py
from flask import Flask, render_template, request
import re

app = Flask(__name__)

def process_input():
    string = request.form['string']
    regex = request.form['regex']
    matches = re.findall(regex, string)
    counts = len(matches)
    return matches, counts

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        matches, counts = process_input()
        return render_template('results.html', matches=matches, count=counts)
    else:
        return render_template('index.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        matches, counts = process_input()
        return render_template('results.html', matches=matches, count=counts)
    else:
        return render_template('results.html')

if __name__ == '__main__':
    app.run()
