# IS 218 Final Project

## Sound Search
Sound search is a Music discovery app that uses Spotify API to dynamically fetch data form Spotify libraries to show top tracks of an Artist. The user will have option to pick an artist through a search bar on page. In case an artist is not picked the page will load top tracks for one of the three pre-selected artists.
User can also add their favourite track by logging in via Google login.

## APIs

  ### 1. [Soptify](https://developer.spotify.com/documentation/general/guides/)
  + *Spotify API is used to obtain top 10 tracks of an artist searched by the user.*
  
  ### 2. [Genius API](https://docs.genius.com/#search-h2)
  
  + *Get song lyrics by passing in the song name*

 ### 3. [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)

  + *Google OAuth 2.0 is used to implement google login (which means users can login via their google accounts)*


## Setup and Installation
**1. Installation**
 * *run following code in terminal to install all the required libraries:*

```bash
  pip install -r requirements.txt
 ```

**2. setup dotenv**
  * *Create a `.env` file in the project directory containing Client id and Client secret in following format:*

```
export sptfy_id = "your spotify client id"
export sptfy_sectret = "your spotify client secret"
export genius_token = "your genius api access token"
export GOOGLE_CLIENT_ID = "your google oAuth cliend id"
export GOOGLE_CLIENT_SECRET = "your google oAuth client secret"
export secret_key = "generate some random string"
```

## Run Application

1. Open up terminal and run command ```python spotify_app.py```
2. Open a new tab in browser and go to 'http://localhost:5000/'

*(Disclaimer: If you are using Grammarly extension in your browser, the app may not work properly. Please open the page in incognito tab or disable Grammarly for the website.)*
