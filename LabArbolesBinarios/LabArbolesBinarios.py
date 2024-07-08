"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

# from LabArbolesBinarios.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

# from LabArbolesBinarios.pages.tools import tools
# from LabArbolesBinarios.pages.team import team
# from LabArbolesBinarios.pages.index import index

# Create app instance and add index page.
# app = rx.App(
#     theme=THEME,
#     stylesheets=STYLESHEETS,
# )

def index() -> rx.Component:
    return rx.stack(
        rx.text("Welcome to the Reflex Lab!",
                class_name={"text-[20px] text-[#156082]"}),
        rx.text("This is the main page of the Reflex Lab."),
        rx.text("You can navigate to the other pages using the links above."),
    )


app = rx.App()
app.add_page(index)
# app.add_page(tools, route="/tools")
# app.add_page(team, route="/team")
