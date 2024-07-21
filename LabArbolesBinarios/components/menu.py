import reflex as rx

from LabArbolesBinarios.controller.class_tree import TreeState

def menu_bar():
    return(
        rx.box(
            rx.box(
                rx.button(
                    rx.text('Color'),
                    on_click=TreeState.change_color,
                    class_name='flex justify-center items-center rounded-none bg-transparent cursor-pointer hover:bg-gray-200',
                ),
            class_name='w-[33%] sm:w-[150px] h-full min-w-[100px]'
            ),
            rx.box(
                rx.popover.root(
                    rx.popover.trigger(
                        rx.button(
                            rx.text('Recorrido'),
                            class_name='flex justify-center items-center rounded-none bg-transparent cursor-pointer hover:bg-gray-200',
                        ),
                    ),
                    rx.popover.content(
                        rx.box(
                            rx.text('Recorrido por niveles', font_weight='700'),
                            rx.text(TreeState.levels),
                            direction='column',
                            class_name='w-[250px] sm:w-full text-center'
                        ),
                        align='center',
                        class_name='w-full max-w-[450px] min-w-[250px] h-full'
                    ),
                ),
                class_name='w-[33%] sm:w-[150px] h-full min-w-[100px]'
            ),
            rx.box(
                rx.button(
                    rx.text('Reiniciar'),
                    on_click=TreeState.reset_tree,
                    class_name='flex justify-center items-center rounded-none bg-transparent cursor-pointer hover:bg-gray-200',
                ),
                class_name='w-[33%] sm:w-[150px] h-full min-w-[100px]'
            ),
            class_name='flex justify-center items-center w-full h-[60px] border-t-[1px] border-b-[1px] border-[#AEAEAE]',
        )
    )