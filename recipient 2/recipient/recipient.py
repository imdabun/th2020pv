import json
from flask import Flask, render_template, request
import os
import time
import requests
app = Flask(__name__, static_url_path='/static')

url = 'https://167.71ß.250.142:5000/page/analy'
result = []

def highestElement(text):
    index = 0
    max = text[0][1]
    for txt in text:
        if(txt[1] > max):
            max = txt[1]
            index = text.index(txt)
    string = text[index][0].replace("\"","") + " "
    print(string, end="")
    return string

@app.route('/analy', methods=['GET'])
def show_results():
        r = requests.get(url)
        words = list(json.loads(r.text))
        result += [highestElement(words)]
        return render_template('recipient.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
