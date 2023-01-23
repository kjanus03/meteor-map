import folium


def create_meteor_icon(color, icon_color):
    icon = folium.Icon(icon='meteor', color=color, icon_color=icon_color, prefix='fa')
    return icon
