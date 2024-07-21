import reflex as rx

def image_avl(src) -> rx.Component:
    return rx.image(
        src = src,
        class_name = 'max-h-[600px]'
    )