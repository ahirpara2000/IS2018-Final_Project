import mysql.connector
import simplejson as json
from flask import Flask, Response
from flask import render_template
from spotify_api import *

app = Flask(__name__)

artist_id = '4YRxDV8wJFPHPTeXepOstw'

@app.route('/')
def index():
    return render_template('index.html', song_info=get_song_info(artist_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
