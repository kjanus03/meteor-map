import folium
from folium.plugins import BeautifyIcon
from folium.plugins import MarkerCluster
import webbrowser
import pandas as pd
from meteor_icon import create_meteor_icon
from description import describe


# Create a map object centered on the point of interest
m = folium.Map(location=[20,0], zoom_start=2)
folium.TileLayer('https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}',
                name='USGS.USTopo',
                attr='Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>').add_to(m)

# Create a marker cluster object
mc = MarkerCluster(max_cluster_radius=18)

# Reading from the meteorite_data.json and ignoring rows without the geolocation
df = pd.DataFrame(pd.read_json("meteorite_data.json"))
df = df[df['geolocation'].notna()]
# Ignoring the rows without the date and correcting it
df = df[df['year'].notna()]
df['year'] = df['year'].apply(lambda x: x[:4])
# Plotting each coordinate
n = len(df)
for i in range(n):
    row = df.iloc[i]
    coordinates = row['geolocation']
    # icon = folium.Icon(icon='meteor', color="lightred", icon_color="black", prefix='fa')
    lat, lon = coordinates.values()
    icon = create_meteor_icon(row['mass'], "black")
    marker = folium.Marker(location=(lat, lon), icon=icon)
    marker.add_child(folium.Popup(describe(row), max_width=300))
    mc.add_child(marker)
m.add_child(mc)
# Save the map object to an HTML file
m.save('my_map.html')

# Open the HTML file in a web browser
webbrowser.open('my_map.html')
