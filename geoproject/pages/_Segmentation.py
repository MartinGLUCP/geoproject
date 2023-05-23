import folium
import streamlit as st
from folium.plugins import Draw

from streamlit_folium import st_folium,folium_static

import leafmap.foliumap as leafmap

#from samgeo import SamGeo, tms_to_geotiff

import numpy as np

@st.cache_data()
def extract_polygon_coordinates(json_data):
    """Function that returns a list of polygon coordinates drawn on the map, from the Json.

    Args:
        json_data (_type_): json file of the draw coordinates

    Returns:
        _type_: list
    """
    coordinates = []
    
    all_drawings = json_data.get("all_drawings", [])
    
    if all_drawings :
        for drawing in all_drawings:
            geometry = drawing.get("geometry", {})
            if geometry.get("type") == "Polygon":
                drawing_coordinates = geometry.get("coordinates", [])
                coordinates.append(drawing_coordinates)

    
    return coordinates

@st.cache_data()
def display_polygons(polygons):
    """Procedure who display the coordinates of polygons (Debug)

    Args:
        polygons (_type_): list
    """
    for i, polygon in enumerate(polygons, 1):
        print(f"Polygon {i}:")
        for j, coordinates in enumerate(polygon, 1):
            print(f"  Coordinates {j}:")
            for coordinate in coordinates:
                print(f"    Lat: {coordinate[1]}, Lng: {coordinate[0]}")

@st.cache_data()
def generate_bounding_boxes(polygons):
    """Function that returns a list of polygon corners coordinates (min & max) drawn on the map, from the Json. -> boundingbox

    Args:
        polygons (_type_): list

    Returns:
        _type_: list
    """
    bounding_boxes = []
    
    for polygon in polygons:
        min_lat = float('inf')
        max_lat = float('-inf')
        min_lng = float('inf')
        max_lng = float('-inf')
        
        for coordinates in polygon:
            for coordinate in coordinates:
                lat, lng = coordinate
                min_lat = min(min_lat, lat)
                max_lat = max(max_lat, lat)
                min_lng = min(min_lng, lng)
                max_lng = max(max_lng, lng)
        
        bounding_box = [min_lat, min_lng, max_lat, max_lng]
        
        bounding_boxes.append(bounding_box)
    
    return bounding_boxes

st.set_page_config(layout="wide")

st.title('Segmentating with SAM on interactive map : (in progress)')

st.info(' The goal here is to select an area on the map with the drawing tools such as the rectangle/polygon, then to make the segmentation of this area. 😉')
st.info(' My main idee was too make the user draw a rectangle on the map, press the segment button then apply SAM, then show the result.')
st.info(' Another idea I had was to simply generate a png of the selected area, then apply SAM on it but taking a screenshot of an interactive map on streamlit with leafmap & folium is not that easy.')
st.info(' Unfortunately running SAM (segmentation anything model) on a web app is not easy, and getting the segmentation to display directly on the interactive map is also complicated.')
st.info(' You can at least do a rectangle on the map, click in segment and see the new map of the zone after couple of seconde')

#Some famous basemap
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Google Terrain': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = True,
        control = True
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
    )
}

#location = paris
m = folium.Map(location=[48.86290791986464, 2.355194091796875],zoom_start = 10)

# Add custom basemaps
basemaps['Google Maps'].add_to(m)
#basemaps['Google Satellite Hybrid'].add_to(m)

Draw(export=True).add_to(m)

c1, c2 = st.columns(2)
with c1:
    output = st_folium(m, width=1400, height=1000)
    save_button=st.button('Segment')

with c2:
    st.write(output)


if save_button:
    st.sidebar.text('Segmentation running')
    
    print(" ")
    polygon_coordinates = extract_polygon_coordinates(output)
    
    display_polygons(polygon_coordinates)

    print(" ")
    
    bounding_boxes = generate_bounding_boxes(polygon_coordinates)
    
    print(bounding_boxes)

    st.markdown("body", unsafe_allow_html=False)

    # Try to apply SAM on interactive map (leafmap)
    if bounding_boxes :
        bbox = bounding_boxes[0]
        m2 = leafmap.Map(center=[bbox[1], bbox[0]], zoom=20)
        m2.add_basemap('SATELLITE')

        #imagesat = 'satellite.tif'
        
        #tms_to_geotiff(output=imagesat, bbox=bbox, zoom=20, source='Satellite')
             
        #m2.add_raster(imagesat, layer_name='Image')
        m2.to_streamlit()
    else :
        print("bbox empty")
