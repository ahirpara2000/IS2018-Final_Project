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

**1. Pre-Requisites**
  1. *Windows 10 Pro, Windows 10 Education Edition, MacOS*
  2. *PyCharm Pro Installed*
  3. *Docker Desktop Installed*

**2. Installation for pycharm and dockers**

  * *Click on add Configuration*
  
  * *Add a new Configuration*
  
  * *Go to dockers and select Docker-compose*
  
  * *Select given ```docker-compose.yml``` file as Compose file*
  
  * *(Optional)*
    + *Select ```--build, force build images```*
    + *Select ```--volumes, remove volumes on down```*

**3. setup dotenv**
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

**Pycharm and Dockers**

1. Click on the green play button on top right, to build and run docker component.
2. Once running, go to 'http://localhost:5000/' in a browser tab.


-- Incase of error that says Dockers container already exists, you can go to ```docker-compose.yml``` and change ```container_name``` for both app and db.

## Features

1. Google login and authentication.
2. Use of Spotify API to look up the top 10 tracks of any artist.
3. Use of genius API to get lyrics for each song.
4. Local database to store user's favorite songs.

## Issues

1. Some of the tracks received from spotify API doesnot have a song preview URL.
2. Some of the tracks don't have lyrics on Genius.

*(Disclaimer: If you are using Grammarly extension in your browser, the app may not work properly. Please open the page in incognito tab or disable Grammarly for the website.)*
