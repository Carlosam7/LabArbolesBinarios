import reflex as rx
from LabArbolesBinarios.components import navbar, menu
#from LabArbolesBinarios.assets.img.logo import logo

def header() -> rx.Component:
    return rx.stack(
        rx.vstack(
            navbar.navbar(),
            rx.box(
                rx.box(
                    rx.image(
                        src= "img/logo/Logotipo.png",
                        height= "50px",
                    ),
                    rx.image(
                        src= "img/logo/Logo_letter.png",
                        height= "10px",
                    ),
                    class_name='flex flex-col items-center space-y-1',
                ),
                menu.menu_bar(),    
                class_name='flex flex-col w-full items-center space-y-4',
            ),
            class_name='flex w-[100%]'
        ),
        class_name='flex w-[100%] lg:sticky lg:top-0 z-50 bg-white'
    )