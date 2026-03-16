#import the fastapi library
from fastapi import FastAPI

#create an instance of the fastapi class
app = FastAPI()

# define a route for the root endpoint
@app.get("/")
def index():
    return {
        "message":"I'm the root"
    }