import requests
import base64
from urllib.parse import urlencode
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