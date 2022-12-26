import os
import telebot
import requests
import json
import csv
import pandas as pd

from apicall_function import get_movie_info

movies_list = []

bot = telebot.TeleBot('5469515437:AAH_UwLWpPXCirV7PBzfTjcLRyHrHKx2yGE')


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message,"Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n"
                """You can use "/help" command to know more about the bot.""")
    

@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message,
                '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: '
                '\"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie '
                'data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global botRunning
    botRunning = True
    bot.reply_to(message, 'Getting movie info...')
    bot.send_message(message.chat.id, 'Movie found!')

    movie_name = message.text

    movie = movie_name.split(' ', 1)[1]

    movie_info = get_movie_info(movie)

    if movie_info:
        message_text = (f"Movie: {movie_info['title']}\n\n" +
                        f"Year of Release: {movie_info['year']}\n\n" +
                        f"IMDb Rating: {movie_info['imdb_rating']}\n\n" +
                        f"Poster Link: {movie_info['poster']}")

        bot.send_message(message.chat.id, message_text)

    else:
        bot.send_message(message.chat.id, 'Movie not found!')
        
    df = pd.DataFrame(movies_list)
    df.to_csv('movies.csv', index=False)

    movie_title = movie_info['title']
    year = movie_info['year']
    imdb_rating = movie_info['imdb_rating']
    movies_data = [movie_title, year, imdb_rating]

    if movies_data not in movies_list:
        movies_list.append(movies_data)
        
    else:
        bot.send_message(message.chat.id, 'Movie already exists in the list!')


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    bot.reply_to(message, 'File generated!')
    fields = ['MOVIE', 'YEAR', 'IMDB RATING']
    with open("movies.csv", 'w+') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(movies_list)
    with open("movies.csv", 'r') as csvfile:
        bot.send_document(message.chat.id, csvfile)


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand ' + '\N{confused face}')


bot.polling()
bot.infinity_polling()
