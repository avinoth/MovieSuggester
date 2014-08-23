from flask import Flask, url_for, redirect, render_template, flash, request
import flask
import random
import urllib
import json

app = Flask(__name__)
app.config.from_object('config')
api_key = app.config["API_KEY"]

baseurl = "https://api.themoviedb.org/3/discover/movie?"
genre = ""
movie = ""
genreid = 0
result = {}

genres= [
    {
      "id": 28,
      "name": "Action"
    },
    {
      "id": 12,
      "name": "Adventure"
    },
    {
      "id": 16,
      "name": "Animation"
    },
    {
      "id": 35,
      "name": "Comedy"
    },
    {
      "id": 80,
      "name": "Crime"
    },
    {
      "id": 105,
      "name": "Disaster"
    },
    {
      "id": 99,
      "name": "Documentary"
    },
    {
      "id": 18,
      "name": "Drama"
    },
    {
      "id": 82,
      "name": "Eastern"
    },
    {
      "id": 2916,
      "name": "Erotic"
    },
    {
      "id": 10751,
      "name": "Family"
    },
    {
      "id": 10750,
      "name": "Fan Film"
    },
    {
      "id": 14,
      "name": "Fantasy"
    },
    {
      "id": 10753,
      "name": "Film Noir"
    },
    {
      "id": 10769,
      "name": "Foreign"
    },
    {
      "id": 36,
      "name": "History"
    },
    {
      "id": 10595,
      "name": "Holiday"
    },
    {
      "id": 27,
      "name": "Horror"
    },
    {
      "id": 10756,
      "name": "Indie"
    },
    {
      "id": 10402,
      "name": "Music"
    },
    {
      "id": 22,
      "name": "Musical"
    },
    {
      "id": 9648,
      "name": "Mystery"
    },
    {
      "id": 10754,
      "name": "Neo-noir"
    },
    {
      "id": 1115,
      "name": "Road Movie"
    },
    {
      "id": 10749,
      "name": "Romance"
    },
    {
      "id": 878,
      "name": "Science Fiction"
    },
    {
      "id": 10755,
      "name": "Short"
    },
    {
      "id": 9805,
      "name": "Sport"
    },
    {
      "id": 10758,
      "name": "Sporting Event"
    },
    {
      "id": 10757,
      "name": "Sports Film"
    },
    {
      "id": 10748,
      "name": "Suspense"
    },
    {
      "id": 10770,
      "name": "TV movie"
    },
    {
      "id": 53,
      "name": "Thriller"
    },
    {
      "id": 10752,
      "name": "War"
    },
    {
      "id": 37,
      "name": "Western"
    }
  ]

@app.route('/', methods = ['GET', 'POST'])
def index():
    output = []
    if request.method == 'GET':
        return flask.render_template('index.html', 
                                 title = "Movie suggester",
                                 genres = genres,
                                 moviename = "Select the options above")
    
    genre = request.form['genre']
    
    for item in genres:
        if item["name"].lower() == genre.lower():
            genreid = item["id"]
    
    if request.form['fromyear'] <= request.form['toyear']:
#we need 10 movies
        for i in range(1, 11):
            
            year = random.randint(int(request.form['fromyear']), int(request.form['toyear']))
            url = baseurl + "api_key=" + api_key + "&with_genres=" + str(genreid) + "&year=" + str(year) + "&vote_average.gt=6.0&vote_count.gte=5"
            resp = urllib.urlopen(url).read()
            jsonvalues = json.loads(resp)  
                
            if jsonvalues['total_pages'] == 0:
                flash ('Seems there is no good movies for the genre year combination, Let\'s do it again..')
                return flask.render_template('index.html', 
                                         title = "Movie suggester",
                                         genres = genres,
                                         moviename = "Select the options above")
            
            elif jsonvalues['total_pages'] > 1:
                page = random.randint(1, jsonvalues['total_pages'])
                resp = urllib.urlopen(url + "&page=" + str(page)).read()
                jsonvalues = json.loads(resp)
        
            movie = str(random.choice(jsonvalues['results'])["title"])
            
            for result in jsonvalues['results']:
                if result['title'] == movie:
                    poster = "http://image.tmdb.org/t/p/w300/" + str(result['poster_path'])
                    
            iurl = "http://www.omdbapi.com/?t=" + movie + "&y=" + str(year)
            resp = urllib.urlopen(iurl).read()
            jsonvalues = json.loads(resp)
            
            if jsonvalues["Response"] == "True":
                movieurl = "www.imdb.com/title/" + jsonvalues["imdbID"]
                result["moviename"] = movie
                result["year"] = year
                result["movieplot"] = jsonvalues["Plot"]
                result["movierating"] = jsonvalues["imdbRating"]
                result["movieurl"] = movieurl
                result["movieposter"] = poster
                                 
            else:
                result["moviename"] = "ErrorOccured"
                result["movieplot"] = "Failed to retrive data from IMDB"
                
            output.append(result)
          
        return flask.render_template('listing.html', 
                                 title = "Movie suggester",
                                 genres = genres,
                                 output = output)
        del output[:]
        
    else:
        flash('From Year should not be greater than To Year')
        return flask.render_template('index.html', 
                                 title = "Movie suggester",
                                 genres = genres,
                                 moviename = "Select the options above")
    
    
    
if __name__ == '__main__':
     app.run()
