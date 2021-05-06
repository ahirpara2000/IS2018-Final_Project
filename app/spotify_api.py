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