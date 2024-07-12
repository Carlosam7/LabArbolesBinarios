import reflex as rx
from typing import Any

def button(text: str, color: str, click:Any) -> rx.Component:
    return rx.button(
        rx.text(text, color = 'white'),
        on_click= click,
        background_color = color,
        border_radius= '0.5em',
        class_name='cursor-pointer'
    )