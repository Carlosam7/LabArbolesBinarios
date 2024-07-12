import reflex as rx

def link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, class_name='hover:text-[#0094FF] text-center'),
        href = url,
        underline= 'none',
        target= '_blank',
    ),