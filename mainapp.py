import urllib
import json
import random

baseurl = "https://api.themoviedb.org/3/discover/movie?"
api_key = "ENTER THEMOVIEDB.ORG API KEY HERE"
genre = ""
genreid = 0
year = 0
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

print "\n\n ******** WELCOME TO WHAT TO WATCH ********\n\n"

def gen_select():
    on_list = False
    
    for item in genres:
        print "%s" % (item["name"].lower(),)
    
    genre = raw_input("\nEnter the genre of the movie you would like to watch,\n Leave blank to select it randomnly>>  ").lower()
    
    for item in genres:
        if item["name"].lower() == genre:
            on_list = True
            
    if genre == "":
        genre = random.choice(genres)["name"].lower()
        print "I have selected %s movies for you, It's good..\n " % (genre,)
        year_select(genre)
    
    elif on_list == False:
        raw_input ("Nope! that's not on the list.. Press return to make the choice again")
        gen_select()
           
    else:
        print "Good that you want to watch %s movies, I like it too..\n" % (genre,)
        year_select(genre)


def year_select(genre):
              
    while True:
        try:
            year = int(raw_input("Now any choice for the year? Type 1 and I ll select it for you >>\n"))
            break
        except ValueError:
            print "Please enter a valid number"
            
    if year == 1:
        year = random.randint(1900, 2014)

    for item in genres:
        if item["name"].lower() == genre:
            genreid = item["id"]

    print "the genre and year area selected,.. they are %s and %d" % (genre, year)
    tmdb_caller(genre, year, genreid)


def tmdb_caller(genre, year, genreid):
    url = baseurl + "api_key=" + api_key + "&with_genres=" + str(genreid) + "&year=" + str(year) + "&vote_average.gt=6.0&vote_count.gte=5"
    resp = urllib.urlopen(url).read()
    jsonvalues = json.loads(resp)  
        
    if jsonvalues['total_pages'] == 0:
        print "Seems there is no good %s movies released in %d" % (genre, year)
        gen_select()
    
    elif jsonvalues['total_pages'] > 1:
        page = random.randint(1, jsonvalues['total_pages'])
        resp = urllib.urlopen(url + "&page=" + str(page)).read()
        jsonvalues = json.loads(resp)
        movie = str(random.choice(jsonvalues['results'])["title"])
        imdb_caller(movie, year)
    
    else:
       movie = str(random.choice(jsonvalues['results'])["title"])
       imdb_caller(movie, year) 
    
      
def imdb_caller(movie, year):
    iurl = "http://www.omdbapi.com/?t=" + movie + "&y=" + str(year)
    resp = urllib.urlopen(iurl).read()
    jsonvalues = json.loads(resp)
    
    if jsonvalues["Response"] == "True":
        print "MOVIE NAME :\t" + movie
        print "MOVIE PLOT: \t" + jsonvalues["Plot"]
        print "MOVIE RATING: \t" + jsonvalues["imdbRating"]
        


if __name__ == "__main__":
    gen_select()


