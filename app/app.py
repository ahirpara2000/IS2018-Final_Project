from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', hello='Hello world!!')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
