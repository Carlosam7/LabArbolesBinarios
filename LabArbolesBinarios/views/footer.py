import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(
                src='/img/logo/Logotipo.png',
                width='50px',
            ),
            rx.image(
                src='/img/logo/Logo_letter.png',
                width='50px',
            ),
            class_name='space-y-1',
        ),
        rx.box(
            rx.link(
                rx.image(
                    src='https://img.icons8.com/?size=100&id=12599&format=png&color=000000',
                    title='GitHub',
                    class_name='w-[30px] h-[30px]',
                ),
                href='https://github.com/Carlosam7',
                target='_blank',
                class_name='cursor-pointer',
            ),
            rx.link(
                rx.image(
                    src='https://img.icons8.com/?size=100&id=118467&format=png&color=000000',
                    title='Facebook',
                    class_name='w-[30px] h-[30px]',
                ),
                href='https://www.facebook.com/',
                target='_blank',
                class_name='cursor-pointer',
            ),
            rx.link(
                rx.image(
                    src='https://img.icons8.com/?size=100&id=32309&format=png&color=000000',
                    title='Instagram',
                    class_name='w-[30px] h-[30px]',
                ),
                href='https://www.instagram.com/cejtech/',
                target='_blank',
                class_name='cursor-pointer',
            ),
            rx.link(
                rx.image(
                    src='https://img.icons8.com/?size=100&id=37326&format=png&color=000000',
                    title='YouTube',
                    class_name='w-[30px] h-[30px]',
                ),
                href='https://www.youtube.com/@carlosarango3786',
                target='_blank',
                class_name='cursor-pointer',
            ),
            class_name='flex items-center justify-center w-full space-x-8',
        ),

        rx.box(
            rx.text('Elaborado por Carlos Arango', color='#000]', text_align='center'),
            rx.text('Barranquilla | Colombia', color='#000', text_align='center', font_weight='bold'),
        ),
        class_name='flex flex-col justify-center items-center w-full bg-[#F5F5F5] space-y-8 p-10 mt-10',
    )