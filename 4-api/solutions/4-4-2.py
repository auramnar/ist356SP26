from fastapi import FastAPI, Body, HTTPException
import requests

apikey = '??'
def tldr_openai(text):
    url = "https://cent.ischool-iot.net/api/genai/chat/completions"
    headers = {
        "X-API-KEY" : apikey
    }
    data = [
 