from fastapi import FastAPI, Query
from app.services import get_location_suggestions, search_local_business

app = FastAPI()

@app.get("/location-suggestions")
def location_suggestions(input: str = Query(...)):
    return get_location_suggestions(input)

@app.get("/search")
def search_business(query: str, location: str = None, lat: float = None, lng: float = None):
    return search_local_business(query, location, lat, lng)
