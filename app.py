from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services import get_location_suggestions, search_local_business

app = FastAPI()

# Allowed origins
origins = [
    "http://localhost:8081",  # Local dev
    "https://serpapi-location-search.onrender.com"  # Render production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Can be true since origins are explicit
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/location-suggestions")
def location_suggestions(input: str = Query(..., description="Input text for location autocomplete")):
    return get_location_suggestions(input)

@app.get("/search")
def search_business(
    query: str = Query(..., description="Search query for business"),
    location: str = Query(None, description="Location name to search businesses in"),
    lat: float = Query(None, description="Latitude coordinate"),
    lng: float = Query(None, description="Longitude coordinate")
):
    if not location and (lat is None or lng is None):
        raise HTTPException(status_code=400, detail="Either 'location' or both 'lat' and 'lng' must be provided")
    return search_local_business(query, location, lat, lng)
