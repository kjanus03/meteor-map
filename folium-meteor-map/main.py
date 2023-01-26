import folium
from folium.plugins import MarkerCluster
import webbrowser
import pandas as pd
from meteor_icon import create_meteor_icon
from description import describe

# Create a map object centered on the point of interest
m = folium.Map(location=[20, 0],
               zoom_start=2,
               max_bounds=True,
               )
# Adding a TileLayer that determines map's visual appearance
folium.TileLayer('https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}',
                 name='USGS.USTopo',
                 attr='Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>',
                 min_zoom=1.6,
                 max_zoom=18
                 ).add_to(m)

# Create a marker cluster object
mc = MarkerCluster(max_cluster_radius=90, show_coverage_on_hover=True, disableClusteringAtZoom=6)

# Reading from the meteorite_data.json and ignoring rows without the geolocation
df = pd.DataFrame(pd.read_json("meteorite_data.json"))
df = df[df['geolocation'].notna()]
# Ignoring the rows without the date and correcting it
df = df[df['year'].notna()]
df['year'] = df['year'].apply(lambda x: x[:4])
# Setting the reccommended class column type to string
df['recclass'] = df['recclass'].astype("string")
# Plotting each coordinate
n = len(df)
for i in range(n):
    row = df.iloc[i]
    coordinates = row['geolocation']
    lat, lon = coordinates.values()
    icon = create_meteor_icon("lightred", "black")
    marker = folium.Marker(location=(lat, lon), icon=icon)
    marker.add_child(folium.Popup(describe(row), max_width=300))
    mc.add_child(marker)
m.add_child(mc)
# Save the map object to an HTML file

m.save('my_map.html')

# Open the HTML file in a web browser
webbrowser.open('my_map.html')
