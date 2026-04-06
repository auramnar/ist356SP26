from fastapi import FastAPI, Body, HTTPException
import requests

apikey = '??'

def tldr_openai(text):
    url = "https://cent.ischool-iot.net/api/genai/chat/completions"
    headers = {
        "X-API-KEY" : apikey
    }

    data = [
        {
            "role": "system",
            "content": '''
            You are a bot that summarizes text in exactly 1 or 2 sentences. 
            You explain the main points simply and clearly at a 5th grade reading level. 
            You only know how to summarize text. 
            '''
        },
        {
            "role": "user",
            "content": "Can you explain how a computer works?"
        },
        {
            "role": "assistant",
            "content": "Sorry I can only summarize text."
        },
        {
            "role": "user",
            "content": "Write a python program that reads a file and prints the first 10 lines."
        },
        {
            "role": "assistant",
            "content": "Sorry I can only summarize text."
        },
        {
            "role": "user",
            "content": text
        }
    ]
    params = { "temperature" : 0.1 }

    response = requests.post(url, headers=headers, json=data, params=params)
    response
    result = response.json()
    return result["choices"][0]["message"]['content']


app = FastAPI()

@app.post("/tldr")
def tldr(text: str = Body(embed=True)):
    '''
    Summarize a URL
    '''
    print(text)
    try:
        return tldr_openai(text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    
# http://localhost:8000/tldr