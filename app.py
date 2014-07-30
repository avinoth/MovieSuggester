from flask import Flask, url_for, redirect, render_template, flash
import flask

app = Flask(__name__)
app.config.from_object('config')
api_key = app.config["API_KEY"]


genres= [
    {
     "id": 120893,
     "name": "Any"
     },
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

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html', 
                                 title = "Hello world",
                                 genres = genres,
                                 moviename = "The Wolf of Wall Street",
                                 movieplot = "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.",
                                 movierating = 8.3,
                                 movieurl = "http://www.imdb.com/title/tt0993846/",
                                 movieposter = "../static/img/portfolio-1.jpg")
    
    
    

if __name__ == '__main__':
    app.run()