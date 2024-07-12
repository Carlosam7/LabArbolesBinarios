import reflex as rx
from LabArbolesBinarios.components.link import link
from LabArbolesBinarios.components.input import input
from LabArbolesBinarios.styles import styles
from LabArbolesBinarios.components.button import button
from LabArbolesBinarios.components.categorias import categorias

def body():
    return rx.box(
        rx.box(
            rx.image(
                src= 'img/tree_avl/image_avl.png',
                class_name='max-h-[600px]'
            ),
            class_name='flex items-center justify-center w-full h-auto'
        ),
        rx.box(
            rx.box(
                link('Ver imagen', '/img/tree_avl/image_avl.png'),
                class_name='flex justify-center items-center w-1/2 text-[14px]'
            ),
            rx.box(
                rx.button(
                    rx.text('Descargar', class_name='hover:text-[#0094FF]'),
                    on_click=rx.download(url='/img/tree_avl/image_avl.png', filename='image_avl.png'),
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
                        background= "center/cover url('Data/cat.160.png')",
                        class_name='w-full h-[40vh] lg:w-[55%] lg:h-full rounded-md shadow-lg'
                    ),
                    rx.box(
                        rx.box(
                            rx.text('Categoría:', font_weight='bold', color='black'),
                            rx.text('Peso:', font_weight='bold', color='black'),
                            rx.text('Nivel:', font_weight='bold', color='black'),
                            rx.text('Fact equilibrio:', font_weight='bold', color='black'),
                            rx.text('Padre:', font_weight='bold', color='black'),
                            rx.text('Abuelo:', font_weight='bold', color='black'),
                            class_name='flex flex-col justify-center items-center w-full text-[1.2em] text-center space-y-5 p-12 bg-[#F5F5F5] lg:h-[70%] lg:items-start rounded-md',
                        ),
                        rx.box(
                            rx.button(
                                rx.text('CAT.160', font_size=styles.Size.BIG.value, font_weight='bold', color='white'),
                                on_click=rx.download(url='/Data/cat.160.png', filename='cat.160.png'),
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