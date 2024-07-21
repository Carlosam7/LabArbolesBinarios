import reflex as rx
from LabArbolesBinarios.components.link import link
from LabArbolesBinarios.components.button import button
from LabArbolesBinarios.styles import styles
# from LabArbolesBinarios.controller.class_tree import FormState
from LabArbolesBinarios.controller.class_tree import TreeState

def navbar() -> rx.Component:
    return rx.box(
            rx.box(
                rx.box(
                    link('GitHub', 'https://github.com/Carlosam7/LabArbolesBinarios.git'),
                    link('YouTube', 'https://www.youtube.com/channel/UCKNH7DQtC9M16VM0kA5AINQ'),
                    class_name= 'flex justify-between w-full lg:justify-start lg:space-x-[60px]'
                ),
                rx.form(
                    rx.box(
                        rx.box(
                            rx.input(
                                placeholder="Nombre del nodo",
                                name='data',
                                variant='soft',
                                color_scheme='gray',
                                font_family='Jura',
                                class_name='flex w-full h-[40px] px-3 rounded-[0.5em] bg-white text-[#6E6E6E]',
                                font_size=styles.Size.SMALL.value,
                            ),
                            class_name='flex w-full rounded-[0.5em] border border-[#4E4E4E] bg-white lg:w-[300px]',
                        ),
                        rx.box(
                            rx.box(
                                button('Add/Delete', '#83CBEB', None),
                                class_name='flex w-full lg:w-auto',
                            ),
                            class_name=f'flex justify-center items-center w-full lg:w-auto '
                        ),
                        class_name=f'flex flex-col items-center justify-center w-full space-y-2 lg:space-x-[{styles.Spacer.MEDIUM.value}] lg:flex-row lg:justify-end lg:space-y-0'
                    ),
                    on_submit=TreeState.handle_submit,
                    reset_on_submit=True,
                ),
                class_name='flex flex-col justify-center w-full h-auto items-center px-12 space-y-4 lg:flex-row lg:justify-between lg:h-[50px] lg:space-y-0'
            ),
        class_name='w-full mb-5 pt-[20px] lg:mb-0'
    )