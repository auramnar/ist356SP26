from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/")    # Define a route for the root URL ("/") that will respond to GET requests
def root():      # Define a function that will be called when the route is requested
    return {"message": "Hello World"} # Serializes to JSON automatically