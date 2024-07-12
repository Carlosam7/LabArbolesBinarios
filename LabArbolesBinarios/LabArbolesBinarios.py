import reflex as rx

from LabArbolesBinarios.views import header, body, footer
from LabArbolesBinarios.styles import styles

def index() -> rx.Component:
    return rx.box(
            rx.vstack(
                header.header(),
                body.body(),
                footer.footer(),
                class_name='flex flex-col w-full items-center justify-center min-w-[300px] max-w-[1720px]'
            ),
            class_name='flex flex-col w-full items-center justify-center min-w-[300px] bg-white'
        )


app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Jura:wght@300..700&display=swap'
    ]
)
app.add_page(index)
# app.add_page(tools, route="/tools")
# app.add_page(team, route="/team")
