import json
from flask import Flask, render_template, request
import os
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return 'Waiting for result...'

@app.route('/result', methods=['GET'])
def show_results():
    q_id = request.args.get('q_id')
    p_id = request.args.get('p_id')
    word = request.args.get('word')
    c_id = request.args.get('c_id')
    return render_template('recipient.html', c_id=c_id, q_id=q_id, \
        p_id=p_id, word=word)


if __name__ == "__main__":
    app.run(debug=True)
