import reflex as rx

def menu_bar():
    return(
        rx.box(
            rx.box(
                rx.button(
                    rx.text('Color'),
                    class_name='flex justify-center items-center rounded-none bg-transparent cursor-pointer hover:bg-gray-200',
                ),
            class_name='w-[33%] sm:w-[150px] h-full min-w-[100px]'
            ),
            rx.box(
                rx.button(
                    rx.text('Recorrido'),
                    class_name='flex justify-center items-center rounded-none bg-transparent cursor-pointer hover:bg-gray-200',
                ),
                class_name='w-[33%] sm:w-[150px] h-full min-w-[100px]'
            ),
            rx.box(
                rx.button(
                    rx.text('Reiniciar'),
                    class_name='flex justify-center items-center rounded-none bg-transparent cursor-pointer hover:bg-gray-200',
                ),
                class_name='w-[33%] sm:w-[150px] h-full min-w-[100px]'
            ),
            class_name='flex justify-center items-center w-full h-[60px] border-t-[1px] border-b-[1px] border-[#AEAEAE]',
        )
    )