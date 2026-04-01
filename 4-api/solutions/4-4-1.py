
#url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"

from fastapi import FastAPI, Query
import pandas as pd
import numpy as np
import json

from streamlit import code

app = FastAPI()

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"
df =pd.read_csv(url)
#print(df.head())
# departure_airport_code
# arrival_airport_code
# KJP, FUN -> departure
# VOG, POW -> arrival

@app.get("/api/search_flights")
def search_flights(type:str =Query(), code:str =Query()):
    if type == "dep":
        flights = df[df["departure_airport_code"] == code]
    elif type == "arr":
        flights = df[df["arrival_airport_code"] == code]
    else:
        return {"error": "Invalid type. should be 'dep' or 'arr'"}

    json_flights = flights.to_json(orient="records")
    return json.loads(json_flights) # python list of dictionaries
