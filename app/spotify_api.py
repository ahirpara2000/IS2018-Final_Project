import requests
import base64
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def get_access_token():
    tocken_url = "https://accounts.spotify.com/api/token"

    creds = f"{os.getenv('sptfy_id')}:{os.getenv('sptfy_sectret')}"

    client_creds = base64.b64encode(creds.encode())

    method = "POST"

    tocken_data = {
        "grant_type": "client_credentials"
    }

    tocken_header = {
        "Authorization": f"Basic {client_creds.decode()}"
    }

    r = requests.post(tocken_url, data=tocken_data, headers=tocken_header)
    tocken_responce = r.json()

    access_token = tocken_responce['access_token']

    return access_token


# get_song_info takes in artist's spotify id as a parameter
# and returns an array of of following format:
# arr[0] : list of artists
# arr[1] : name if the song/track
# arr[2] : preview url of the song/track
# arr[3] : image related to song

def get_song_info(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks" + "?" + "market=US"

    method = "POST"

    request_header = {
        "Authorization": f"Bearer {get_access_token()}"
    }

    response = requests.get(url, headers=request_header)
    results = response.json();

    song_info = []

    count = 0

    for track in results['tracks']:
        song_info.append([[]])
        for i in range(len(track['artists'])):
            song_info[count][0].append(track['artists'][i]['name'])
        song_info[count].append(track['name'])
        song_info[count].append(track['preview_url'])
        song_info[count].append(track['album']['images'][0]['url'])
        count += 1

    return song_info


# get_artist takes in artist's spotify id as a parameter
# and returns name of the artist as a string

def get_artist(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    method = "GET"
    request_header = {
        "Authorization": f"Bearer {get_access_token()}"
    }
    response = requests.get(url, headers=request_header)
    results = response.json();

    artist_info = results['name']

    return artist_info


# get_artist_id takes artist name as a parameter
# and returns artist id if found
# or returns error code if artist is not found

def get_artist_id(name):
    url = "https://api.spotify.com/v1/search"
    mehod = "GET"

    request_header = {
        "Authorization": f"Bearer {get_access_token()}"
    }

    # makes a url ready query paramater

    query_param = urlencode({
        "q": name,
        "type": "artist",
        "limit": "1"
    })

    url_lookup = f"{url}?{query_param}"  # creates a lookup url

    response = requests.get(url_lookup, headers=request_header)  # makes the request

    # if the request is in jason format,
    # and it contains Artist Id, then the artist id is returns as a string
    # else a status code is returned as an int

    try:
        results = response.json()
        return results["artists"]["items"][0]["id"]
    except:
        results = response.status_code
        return results
