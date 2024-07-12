from enum import Enum
import reflex as rx

# Sizes
class Spacer(Enum):
    SMALL = '0.5em'
    MEDIUM = '1em'
    BIG = '2em'

class Size(Enum):
    SMALL = '0.8em'
    MEDIUM = '1em'
    BIG = '1.5em'


BASE_STYLE = {
    rx.button: {
        'width': '100%',
        'height': '100%',
        'padding_y': Size.SMALL.value,
        'padding_x': Size.BIG.value,
    },
    rx.text: {
        'font_size': Size.MEDIUM.value,
        'font-family': 'Jura',
        'color': '#6E6E6E',
        'font-weight': '620',
    }
    
}