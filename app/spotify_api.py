# import requests
import base64
from urllib.parse import urlencode
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

def printSpotify():
    return os.getenv('sptfy_id')