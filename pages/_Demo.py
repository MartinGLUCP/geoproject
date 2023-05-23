import streamlit as st
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")

st.title('Observation of different map :')
st.info(' A page to demonstrate the capabilities of leafmap. to be able to select many basemaps (some do not work).')
col1,col2 = st.columns([4,1])

options = list(leafmap.basemaps.keys())

with col2:
    dropdown = st.selectbox("Basemap",options )
    #dropdown = st.selectbox("Basemap",["HYBRID","ROADMAP","TERRAIN"])
    
    default_url = leafmap.basemaps[dropdown].tiles

    url = st.text_input("Enter URL",default_url)

m = leafmap.Map()
m.add_basemap(dropdown)
if url:
    m.add_tile_layer(url,name='Tile layer',attribution=' ')
with col1 :
    m.to_streamlit()
  


#Trying to save the map
#m.save('map.jpg')
#to_image(m)
#m.to_html("map.html")
#m._to_png()
#m.to_image()
#print(bbox)
#save_map(m)