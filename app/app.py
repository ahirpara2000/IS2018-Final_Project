from flask import Flask, render_template, request, url_for, session, redirect
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv, find_dotenv
import random
import spotify_api
import os
from datetime import timedelta

load_dotenv(find_dotenv())

app = Flask(__name__)

# artist list: [Arijit Singh, Armaan Malik, A.R. Rahman]

artist = ['4YRxDV8wJFPHPTeXepOstw',
          '4IKVDbCSBTxBeAsMKjAuTs',
          '1mYsTxnqsietFxj1OgoGbG']

app.secret_key = os.getenv('secret_key')
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def run():
    session['is_authorized'] = False
    return render_template(
        "login.html",
    )

@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['is_authorized'] = True
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/artist')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@app.route('/artist', methods=["GET", "POST"])
def artist_search():
    if not session.get('is_authorized'):
        return redirect('/')

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
            len=len(song_info),  # array length
            len2=len(song_info[0]),  # array length for artists
            song_info=song_info,  # array
            artist_name=spotify_api.get_artist(artist_id)  # gets artist's name
        )
    else:
        song_info = spotify_api.get_song_info(artist_id)  # gets artist info as an array (user picked aritst)

        if (len(song_info) > 0):
            artist_len = len(song_info[0])
        else:
            artist_len = 0

        return render_template(
            "index.html",
            len=len(song_info),  # array length
            len2=artist_len,  # array length for artists
            song_info=song_info,  # array
            artist_name=spotify_api.get_artist(artist_id)  # gets artist's name
        )


@app.route('/lyrics/<song_name>/<artist_name>')
def lyrics(song_name, artist_name):
    artist_name = artist_name[14:]
    print(artist_name)
    try:
        lyrics = spotify_api.get_lyrics(song_name, artist_name)
    except:
        lyrics = "Opps no lyrics found..!!"

    return {
        'Lyrics': lyrics
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0')
