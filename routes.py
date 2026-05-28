#!/usr/bin/env python3
import os
import requests
import polyline
from dotenv import load_dotenv
load_dotenv()

def query_route(coo_a, coo_b):

    base_url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        #"Authorization": os.environ.get("OPENROUTE_API_KEY")
        "Accept": "application/geo+json; charset=utf-8"
        }

    body = {
        "coordinates": [coo_a, coo_b]
            #[2.1734, 41.3851],  # Barcelona
            #[2.2945, 48.8584]   # Paris
}
    api_key = os.environ.get("OPENROUTE_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTE_API_KEY environment variable is not set.")
    url = base_url + "?api_key=" + api_key + "&start=" + str(coo_a[0]) + "," + str(coo_a[1]) + "&end=" + str(coo_b[0]) + "," + str(coo_b[1])
    response = requests.post(url, json=body, headers=headers)
    route_coords = []
    for coords in polyline.decode(response.json()["routes"][0]["geometry"]):
            route_coords.append([coords[0], coords[1]])

    return route_coords
    

if __name__ == "__main__":
    start = [2.1557, 41.3921]
    end = [2.1312, 41.3887]
    route = query_route(start, end)
    print(route)
    print("end ...")