from math import log10, ceil, isnan
from IPython.core.display import HTML
from folium import DivIcon

def iconSize(mass):
    if isnan(mass):
        result = 3
    else:
        result = 3*ceil(log10(mass))
    return result

def create_meteor_icon(mass, color):
    size = iconSize(mass)
    print(size)
    html = f"""
            <div style="width:{size}px; height:{size}px">
            <i class="fas fa-meteor" style="color:{color}"></i>
            </div>
        """

    return DivIcon(html=html)


