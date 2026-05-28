#!/usr/bin/env python3
import os
import streamlit as st
import folium
from routes import query_route
from streamlit_folium import st_folium

def update_map(start_lat, start_lon, end_lat, end_lon, route_coords=None):
        mid_lat = (start_lat+end_lat) * 0.5
        mid_lon = (start_lon+end_lon) * 0.5
        m = folium.Map(location=[mid_lat, mid_lon], tiles="CartoDB positron", zoom_start=14)

        # Add a marker to the map
        folium.Marker(
                location = [start_lat, start_lon], 
                popup = "start",
                icon = folium.Icon(icon="play",color="darkgreen") 
                ).add_to(m)

        folium.Marker(
                location = [end_lat, end_lon], 
                popup = "End",
                icon = folium.Icon(color="red") 
                ).add_to(m)
        if route_coords:
             folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(m)
        return m


if __name__ == "__main__":

    st.set_page_config(page_title="Demo Maps", page_icon=":map:", layout="wide")

    st.title("Route between two points")
    
    coord_start = st.text_input("Enter the starting coordinates (latitude, longitude):", "41.4013 , 2.1517")
    start_lat = float(coord_start.split(",")[0])
    start_lon = float(coord_start.split(",")[1])
    coord_end = st.text_input("Enter the ending coordinates (latitude, longitude):", "41.3887, 2.1312")
    end_lat = float(coord_end.split(",")[0])
    end_lon = float(coord_end.split(",")[1])


    # Keep route across reruns
    if "route_coords" not in st.session_state:
        st.session_state.route_coords = None

           
    if st.button("Calculate Route"):
        try:
            st.session_state.route_coords = query_route([start_lon, start_lat], 
                                                        [end_lon, end_lat])
            st.success("Route calculated successfully!")
        except Exception as e:
            st.error(f"Error calculating route: {e}")
            st.session_state.route_coords = None
    
    m = update_map(start_lat, start_lon, end_lat, end_lon, st.session_state.route_coords)
    st_folium(m, width=1080, height=300)