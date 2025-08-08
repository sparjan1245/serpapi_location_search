# services.py
import os
import requests
from dotenv import load_dotenv
from typing import Optional, List, Dict, Any

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
def get_location_suggestions(input_text: str) -> List[str]:
    """Get autocomplete suggestions for a location in India from SerpAPI"""
    params = {
        "engine": "google_autocomplete",
        "q": input_text,
        "gl": "in",              # Restrict to India
        "api_key": SERPAPI_KEY,
    }
    res = requests.get("https://serpapi.com/search", params=params)
    res.raise_for_status()
    suggestions = res.json().get("suggestions", [])
    return suggestions


def search_local_business(query: str, location: Optional[str] = None,
                          lat: Optional[float] = None, lng: Optional[float] = None) -> List[Dict[str, Any]]:
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
        raise ValueError("Missing location or coordinates")

    res = requests.get("https://serpapi.com/search.json", params=params)
    res.raise_for_status()
    results = res.json().get("local_results", [])
    return results
