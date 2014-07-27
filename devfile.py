import urllib
import json
import random

url = "https://api.themoviedb.org/3/discover/movie?api_key=b38d52928554b4c9fe0b7b43f36a3c7b&with_genres=28&year=2011&sort_by=popularity.desc"

resp = urllib.urlopen(url).read()
jsonvalues = json.loads(resp)


page = random.randint(1, jsonvalues['total_pages'])

resp = urllib.urlopen(url + "&page=" + str(page)).read()
jsonvalues = json.loads(resp)
print jsonvalues