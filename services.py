import os
import requests
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def get_location_suggestions(input_text):
    """Get autocomplete suggestions for a location from SerpAPI"""
    params = {
        "engine": "google_autocomplete",
        "q": input_text,
        "api_key": SERPAPI_KEY
    }
    res = requests.get("https://serpapi.com/search", params=params)
    suggestions = res.json().get("suggestions", [])
    return suggestions

def search_local_business(query, location=None, lat=None, lng=None):
    """Search local businesses by location name or coordinates via SerpAPI"""
    if location:
        params = {
            "engine": "google_local",
            "q": query,
            "location": location,
            "api_key": SERPAPI_KEY
        }
    elif lat is not None and lng is not None:
        params = {
            "engine": "google_maps",
            "q": query,
            "ll": f"@{lat},{lng},14z",
            "api_key": SERPAPI_KEY
        }
    else:
        return {"error": "Missing location or coordinates"}

    res = requests.get("https://serpapi.com/search.json", params=params)
    results = res.json().get("local_results", [])
    return results
