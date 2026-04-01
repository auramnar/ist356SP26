from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/")    # Define a route for the root URL ("/") that will respond to GET requests
def root():      # Define a function that will be called when the route is requested
    return {"message": "Hello World"} # Serializes to JSON automatically

@app.get("/hi/{name}") # Define a route with a path parameter "name"
def say_hi(name: str): # Define a function that takes the path parameter "name"
    return {"message": f"Hi {name}"} # Return a personalized greeting message


@app.get("/roll/{number}/d/{sides}")
def roll_dice(number: int, sides: int):
    import random 
    rolls = random.randint(1, sides) * number
    return {
        "number_of_rolls": number,
        "number_of_sides": sides,
        "total of rolls": rolls
    }
