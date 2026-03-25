import requests 
import requests_cache as rq
import pickle

texts = [
    "I love IST356. It is the best course I've ever taken.", 
    "I hate the New York Giants.",
    "I love IST256. It is the best course I've ever taken.", 
    "I don't like the New York Giants."
]


apikey = "632985c9646a0bc8f547f1d9"
headers = {'X-API-KEY': apikey}
url ="https://cent.ischool-iot.net/api/azure/sentiment"


cache = rq.clear_cache('sentiment.pkl')

for text in texts: # loop over each string in the list
    if text in cache: # check if text was analyzed before and is in cache
        results =cache[text]
        from_cache = "CACHED"
