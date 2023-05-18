"""Main module."""

import string
import random
import ipyleaflet

class Map(ipyleaflet.Map):
   
    def __init__(self, center, zoom, **kwargs) -> None:
        if "scroll_wheel_zoom" not in kwargs:
            kwargs["scroll_wheel_zoom"] = True
        super().__init__(center=center, zoom=zoom, **kwargs)
    
    def add_search_control(self, **kwargs):
        """add search button
        """        
        search_control = ipyleaflet.SearchControl(**kwargs)
        self.add_control(search_control)

    def add_draw_control(self, **kwargs):
        """add all draw buttons
        """        
        draw_control = ipyleaflet.DrawControl(**kwargs)

        draw_control.polyline =  {
            "shapeOptions": {
                "color": "#6bc2e5",
                "weight": 8,
                "opacity": 1.0
            }
        }
        draw_control.polygon = {
            "shapeOptions": {
                "fillColor": "#6be5c3",
                "color": "#6be5c3",
                "fillOpacity": 1.0
            },
            "drawError": {
                "color": "#dd253b",
                "message": "Oups!"
            },
            "allowIntersection": False
        }
        draw_control.circle = {
            "shapeOptions": {
                "fillColor": "#efed69",
                "color": "#efed69",
                "fillOpacity": 1.0
            }
        }
        draw_control.rectangle = {
            "shapeOptions": {
                "fillColor": "#fca45d",
                "color": "#fca45d",
                "fillOpacity": 1.0
            }
        }

        self.add_control(draw_control)

def generate_random_string(length):
    """Generate random string"""
    characters = string.ascii_letters + string.digits  # Includes both uppercase and lowercase letters, and digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_lucky_number(length=1):
    """_summary_

    Args:
        length (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
    random_string = ''.join(random.choice(string.digits) for _ in range(length))
    return int(random_string)