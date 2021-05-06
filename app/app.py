from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv, find_dotenv
import os
import random
import spotify_api

app = Flask(__name__)

load_dotenv(find_dotenv())

# artist list: [Arijit Singh, Armaan Malik, A.R. Rahman]

artist = ['4YRxDV8wJFPHPTeXepOstw',
          '4IKVDbCSBTxBeAsMKjAuTs',
          '1mYsTxnqsietFxj1OgoGbG']


@app.route('/')
def run():
    artist_id = random.choice(artist)
    song_info = spotify_api.get_song_info(artist_id)
    return render_template(
        "index.html",
        len=len(song_info),
        len2=len(song_info[0]),
        song_info=song_info,
        artist_name=spotify_api.get_artist(artist_id)
    )


@app.route('/artist', methods=["GET", "POST"])
def artist_search():
    if request.method == "POST":
        name = request.form.get("a_name")  # get's artist name form html form
        artist_id = spotify_api.get_artist_id(name)  # pass in artist name and gets artist id

    else:
        artist_id = random.choice(artist)  # randomly choose an artist

    if (isinstance(artist_id, int) or artist_id == ''):
        artist_id = random.choice(artist)  # randomly choose an artist
        song_info = spotify_api.get_song_info(artist_id)  # gets artist info as an array (random aritst)
        return render_template(
            "index.html",
            err_msg=True,  # error message
            song_info=song_info,  # array
            artist_name=spotify_api.get_artist(artist_id)  # gets artist's name
        )
    else:
        song_info = spotify_api.get_song_info(artist_id)  # gets artist info as an array (user picked aritst)

        return render_template(
            "index.html",
            song_info=song_info,  # array
            artist_name=spotify_api.get_artist(artist_id)  # gets artist's name
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
