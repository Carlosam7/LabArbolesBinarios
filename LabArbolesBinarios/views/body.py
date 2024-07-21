import reflex as rx
from LabArbolesBinarios.components.link import link
from LabArbolesBinarios.components.input import input
from LabArbolesBinarios.styles import styles
from LabArbolesBinarios.components.categorias import categorias
from LabArbolesBinarios.components.image_avl import image_avl
from LabArbolesBinarios.controller.class_tree import TreeState
from LabArbolesBinarios.controller.info_node import InfoNode


def body():
    return rx.box(
        rx.box(
            image_avl(TreeState.img_avl),
        ),
        rx.box(
            rx.box(
                link('Ver imagen', TreeState.img_avl),
                class_name='flex justify-center items-center w-1/2 text-[14px]'
            ),
            rx.box(
                rx.button(
                    rx.text('Descargar', class_name='hover:text-[#0094FF]'),
                    on_click=rx.download(url=TreeState.img_avl, filename='image_avl.png'),
                    class_name='w-auto px-0 py-0 bg-transparent cursor-pointer'
                ),
                class_name='flex justify-center items-center w-1/2'
            ),
            class_name='flex items-center justify-center w-full sm:w-[300px]'
        ),
        rx.box(
            input('Buscar nodo', 'search'),
            rx.box(
                rx.box(
                    rx.text(
                        'Información del nodo',
                        color='#000',
                        font_size=styles.Size.BIG.value,
                        font_weight='bold',
                    ),
                    rx.text(
                        'A continuación se presenta imagen (si la tiene) y demás información perteneciente al nodo consultado.',
                        font_size=styles.Size.SMALL.value,
                        class_name='min-w-[300px] px-5 w-[70%] text-center'
                    ),
                    class_name='flex flex-col items-center w-full space-y-2'
                ),
                rx.box(
                    rx.box(
                        background= f"center/cover url({InfoNode.src})",
                        class_name='w-full h-[40vh] lg:w-[55%] lg:h-full rounded-md shadow-lg'
                    ),
                    rx.box(
                        rx.box(
                            rx.text(f'Categoría: {InfoNode.categoria}', font_weight='bold', color='black'),
                            rx.text(f'Peso: {InfoNode.peso}', font_weight='bold', color='black'),
                            rx.text(f'Nivel: {InfoNode.nivel}', font_weight='bold', color='black'),
                            rx.text(f'Fact equilibrio: {InfoNode.factor_equilibrio}', font_weight='bold', color='black'),
                            rx.text(f'Padre: {InfoNode.padre}', font_weight='bold', color='black'),
                            rx.text(f'Abuelo: {InfoNode.abuelo}', font_weight='bold', color='black'),
                            class_name='flex flex-col justify-center items-center w-full text-[1.2em] text-center space-y-5 p-12 bg-[#F5F5F5] lg:h-[70%] lg:items-start rounded-md',
                        ),
                        rx.box(
                            rx.button(
                                rx.text(InfoNode.data, font_size=styles.Size.BIG.value, font_weight='bold', color='white'),
                                on_click=rx.download(url=InfoNode.src, filename=InfoNode.data),
                                class_name='flex items-center justify-center w-full h-[70px] bg-[#83CBEB] lg:h-[30%] cursor-pointer'
                            ),
                            class_name='flex items-center justify-center w-full h-[70px] bg-[#83CBEB] lg:h-[30%] rounded-md'
                        ),
                        class_name='flex flex-col items-start w-full space-y-4 lg:w-[45%] lg:h-full'
                    ),
                    class_name='flex flex-col items-center w-full space-y-4 lg:flex-row lg:h-[550px] lg:space-x-4 lg:space-y-0'
                ),
                class_name='flex flex-col items-center w-full space-y-8'
            ),
            categorias(),
            class_name='flex flex-col items-center justify-center w-full md:w-[60%] space-y-20'
        ),
        class_name='flex flex-col w-full items-center justify-center space-y-8 p-5'
    ),