import reflex as rx

def input(placeholder: str, icon: str) -> rx.Component:
    return rx.box(
                    rx.icon(icon, class_name='w-[20px] h-[20px] bg-white mx-3', color='#353C43'),
                    rx.input(
                        placeholder=placeholder,
                        variant='soft',
                        color_scheme='gray',
                        font_family='Jura',
                        class_name='w-full h-[45px] rounded-l-[0px] bg-white text-[#6E6E6E]',
                    ),
                    class_name='flex items-center justify-center w-full border-[1px] border-[#4E4E4E] rounded-md'
                ),