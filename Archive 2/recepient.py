import json
import webbrowser

from flask import Flask, render_template, request
import os
import time
import requests
import tkinter as tk
from tkinter import messagebox
app = Flask(__name__, static_url_path='/static')

link = "http://167.71.250.142:5000/page/"
str2 = "end"
result = []

def highestElement(text):
    index = 0
    max = text[0][1]
    for txt in text:
        if(txt[1] > max):
            max = txt[1]
            index = text.index(txt)
    string = text[index][0].replace("\"","")
    print(string, end="")
    return str(string)


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1

#@app.route('/page/result', methods=['GET'])
def show_results():
    r = requests.get(link + str2)
    words = list(json.loads(r.text))
    #print(words)
    if(len(words) > 0):
        result.append(highestElement(words))

    result2 = result.copy()
    result2 = listToString(result2) + " "
    #print(result2)
    html_str = f"""<!doctype html>
                <html>
<meta charset="utf-8">
<head>
<title>Recipient</title>
<link rel= "stylesheet" type= "text/css" href="static/recipient.css">

</head>
<body>
<p>
  Printed text: {result2}
</p>

</body>
</html>
"""
    Html_file = open("recipient.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    webbrowser.open('file://' + os.path.realpath('recipient.html'),0,True)
    #return render_template('recipient.html', result=result)

if __name__ == "__main__":
    secondInit = time.time()
    while True:
        second = time.time()
        second -= secondInit
        if (float(second) % 6 > 5.95):
            os.system("killall -9 'Google Chrome'")
        if (float(second) % 6 == 0):
            show_results()
