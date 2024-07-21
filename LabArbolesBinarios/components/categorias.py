import reflex as rx
from LabArbolesBinarios.styles import styles

def categorias() -> rx.Component:
    return rx.box(
                rx.box(
                    rx.text(
                        'Categorías',
                        color='#000',
                        font_size=styles.Size.BIG.value,
                        font_weight='bold',
                    ),
                    class_name='flex items-center justify-center w-full'
                ),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.text(
                                    'HUMAN',
                                    color='white',
                                    font_weight='bold',
                                    class_name='absolute z-10'
                                ),
                                rx.box(
                                    class_name='flex items-center justify-center w-full h-full bg-[#00C077] opacity-70 rounded-md'
                                ),
                                background= "top/cover url('Data/rider-202.png')",
                                class_name='flex items-center justify-center w-[60%] h-full] rounded-md shadow-lg'
                            ),
                            rx.box(
                                rx.box(
                                    rx.text(
                                        'CAT',
                                        color='white',
                                        font_weight='bold',
                                        class_name='absolute z-10'
                                    ),
                                    rx.box(
                                        class_name='flex items-center justify-center w-full h-full bg-[#FF5205] opacity-70 rounded-md'
                                    ),
                                    background= "top/cover url('Data/cat.54.png')",
                                    class_name='flex items-center justify-center w-full h-[60%] rounded-md shadow-lg'
                                ),
                                rx.box(
                                    rx.text(
                                        'FLOWERS',
                                        color='white',
                                        font_weight='bold',
                                        class_name='absolute z-10'
                                    ),
                                    rx.box(
                                        class_name='flex items-center justify-center w-full h-full bg-[#FF71FC] opacity-70 rounded-md'
                                    ),
                                    background= "top/cover url('Data/0137.png')",
                                    class_name='flex items-center justify-center w-full h-[40%] rounded-md shadow-lg'
                                ),
                                class_name='flex flex-col w-[40%] h-full space-y-2 lg:space-y-4'
                            ),
                            class_name='flex w-full h-[70%] space-x-2 lg:space-x-4'
                        ),
                        rx.box(
                            rx.box(
                                rx.text(
                                    'CARS',
                                    color='white',
                                    font_weight='bold',
                                    class_name='absolute z-10'
                                ),
                                rx.box(
                                    class_name='flex items-center justify-center w-full h-full bg-[#404040] opacity-70 rounded-md'
                                ),
                                background= "top/cover url('Data/carsgraz_288.bmp')",
                                class_name='flex items-center justify-center w-[50%] h-full rounded-md shadow-lg'
                            ),
                            rx.box(
                                rx.text(
                                    'HORSE',
                                    color='white',
                                    font_weight='bold',
                                    class_name='absolute z-10'
                                ),
                                rx.box(
                                    class_name='flex items-center justify-center w-full h-full bg-[#FFC000] opacity-70 rounded-md'
                                ),
                                background= "top/cover url('Data/horse-202.png')",
                                class_name='flex items-center justify-center w-[50%] h-full rounded-md shadow-lg'
                            ),
                            class_name='flex w-full h-[30%] space-x-2 lg:space-x-4'
                        ),
                        class_name='flex flex-col w-full h-[500px] space-y-2 lg:w-[70%] lg:space-y-4'
                    ),
                    rx.box(
                        rx.box(
                            rx.text(
                                'BIKE',
                                color='white',
                                font_weight='bold',
                                class_name='absolute z-10'
                            ),
                            rx.box(
                                class_name='flex items-center justify-center w-full h-full bg-[#057CFF] opacity-70 rounded-md'
                            ),
                            background= "top/cover url('Data/bike_335.bmp')",
                            class_name='flex items-center justify-center w-full rounded-md shadow-lg lg:h-[35%]'
                        ),
                        rx.box(
                            rx.text(
                                    'DOG',
                                    color='white',
                                    font_weight='bold',
                                    class_name='absolute z-10'
                                ),
                            rx.box(
                                class_name='flex items-center justify-center w-full h-full bg-[#F2006D] opacity-70 rounded-md'
                            ),
                            
                            background= "top/cover url('Data/dog.101.jpg')",
                            class_name='flex items-center justify-center w-full rounded-md shadow-lg lg:h-[65%]'
                        ),
                        class_name='flex w-full h-[250px] space-x-2 lg:flex-col lg:w-[30%] lg:h-[500px] lg:space-x-0 lg:space-y-4'
                    ),
                    class_name='flex flex-col lg:flex-row items-center justify-center w-full h-[500px] space-y-2 lg:space-y-0 lg:space-x-4'
                ),
                class_name='flex flex-col w-full space-y-8'
            ),