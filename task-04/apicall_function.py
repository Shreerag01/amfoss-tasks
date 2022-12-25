import os
import requests

def get_movie_info(movieTitle):
    url = 'http://www.omdbapi.com/?i=tt3896198&apikey=873a80d5'
    api_key = os.getenv('873a80d5')
    data = {'apikey': api_key, 't': movieTitle}
    response = requests.get(url, data)

    if response.status_code != 200:
        return None

    data = response.json()

    movie_info = {"title": data["Title"], "year": data["Year"], "imdb_rating": data["imdbRating"], "poster": data["Poster"]}

    return movie_info
