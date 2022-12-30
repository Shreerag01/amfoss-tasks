import os
import requests

def get_movie_info(movieTitle):
    # Replace API key placeholder with your actual API key
    api_key = '873a80d5'
    url = 'http://www.omdbapi.com/'
    data = {'apikey': api_key, 't': movieTitle}
    response = requests.get(url, data)

    if response.status_code != 200:
        return None

    data = response.json()

    movie_info = {"title": data["Title"], "year": data["Year"], "imdb_rating": data["imdbRating"], "poster": data["Poster"]}

    return movie_info