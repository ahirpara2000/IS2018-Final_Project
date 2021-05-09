from flask import Flask, render_template, request, url_for, session, redirect
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv, find_dotenv
import random
import spotify_api
import os
from flaskext.mysql import MySQL
from datetime import timedelta
from pymysql.cursors import DictCursor

load_dotenv(find_dotenv())

app = Flask(__name__)

# artist list: [Arijit Singh, Armaan Malik, A.R. Rahman]

artist = ['4YRxDV8wJFPHPTeXepOstw',
          '4IKVDbCSBTxBeAsMKjAuTs',
          '1mYsTxnqsietFxj1OgoGbG']

app.secret_key = os.getenv('secret_key')
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'favoritesData'
mysql.init_app(app)

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
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
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
    session['curr_user'] = user_info['id']

    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM userData WHERE user_id=%s', user_info['id'])
    num_rows = cursor.rowcount

    if num_rows == 0:
        inputData = (user_info['id'], user_info['given_name'], user_info['family_name'])
        sql_insert_query = """INSERT INTO userData (user_id,first_name,last_name) VALUES (%s, %s,%s) """
        cursor.execute(sql_insert_query, inputData)
        mysql.get_db().commit()

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

    global song_info

    if isinstance(artist_id, int) or artist_id == '':
        artist_id = random.choice(artist)  # randomly choose an artist
        song_info = spotify_api.get_song_info(artist_id)  # gets artist info as an array (random aritst)
        return render_template(
            "index.html",
            err_msg=True,  # error message
            len=len(song_info),  # array length
            len2=len(song_info[0]),  # array length for artists
            song_info=song_info,  # array
            artist_name=spotify_api.get_artist(artist_id)
        )
    else:
        song_info = spotify_api.get_song_info(artist_id)  # gets artist info as an array (user picked aritst)

        if len(song_info) > 0:
            artist_len = len(song_info[0])
        else:
            artist_len = 0

        return render_template(
            "index.html",
            len=len(song_info),  # array length
            len2=artist_len,  # array length for artists
            song_info=song_info,  # array
            artist_name=spotify_api.get_artist(artist_id)
        )

@app.route('/favourite')
def favourite():
    if not session.get('is_authorized'):
        return redirect('/')

    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM favorits WHERE user_id=%s', session.get('curr_user'))
    results = cursor.fetchall()
    song_info = []
    print(results)
    for song in results:
        temp = []
        temp.append(song['artist_name'])
        temp.append(song['song_name'])
        temp.append(song['song_link'])
        temp.append(song['song_image'])
        song_info.append(temp)
    print(song_info)
    return render_template('favourite.html', song_info=song_info, len=len(song_info))

@app.route('/lyrics/<song_name>/<artist_name>')
def lyrics(song_name, artist_name):
    artist_name = artist_name[14:]
    try:
        lyrics = spotify_api.get_lyrics(song_name, artist_name)
    except:
        lyrics = "Opps no lyrics found..!!"

    return {
        'Lyrics': lyrics
    }


@app.route('/addtofav/<data>')
def add_to_fav(data):
    global song_info
    data = int(data)

    selected_song = song_info[int(data)]

    cursor = mysql.get_db().cursor()

    cursor.execute('SELECT * FROM favorits WHERE user_id=%s AND song_name=%s',
                   (session.get('curr_user'), selected_song[1]))
    num_rows = cursor.rowcount

    if num_rows == 0:
        inputData = (
            session.get('curr_user'), selected_song[1], selected_song[2], selected_song[3], selected_song[0][0])
        sql_insert_query = """INSERT INTO favorits (user_id,song_name,song_link, song_image, artist_name) VALUES (%s, %s,%s, %s ,%s) """

        cursor.execute(sql_insert_query, inputData)
        mysql.get_db().commit()

    return '200'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
