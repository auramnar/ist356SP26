import requests 
import requests_cache as rq
import pickle

texts = [
    "I love IST356. It is the best course I've ever taken.", 
    "I hate the New York Giants.",
    "I love IST256. It is the best course I've ever taken.", 
    "I don't like the New York Giants."
]

cache = rq.load_cache('sentiment.pkl')# open and deserialize sentiment.pkl

apikey = "632985c9646a0bc8f547f1d9"
headers = {'X-API-KEY': apikey}
url ="https://cent.ischool-iot.net/api/azure/sentiment"

# Loop over each string in the list
for text in texts: 
    if text in cache: # check if text was analyzed before and is in cache
        results =cache[text]
        from_cache = "CACHED" # add a label to indicate the result is from cache
    else: # if text is not in the cache then call the API
        data = {'text': text} # create a key/value to send to the API
        
        response = requests.post(url, headers=headers, data=data)
        results = response.json()
        cache[text] = results # save the result for reuse later
        rq.save_cache(cache, 'sentiment.pkl') # write the updated cache to the pickle file
        from_cache = "NOT CACHED" # add a label to indicate that the result was not from the cache
        
        
    sentiment = results['results']['documents'][0]['sentiment'] # extract the sentiment from the nested json response
    print(text, sentiment, from_cache) # print text analyzed , sentiment and cache status