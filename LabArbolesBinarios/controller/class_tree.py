import reflex as rx
import random
import os
from shutil import rmtree
import asyncio

from LabArbolesBinarios.classes.Avl import Avl
from LabArbolesBinarios.components.image_avl import image_avl

T = Avl(None)

class TreeState(rx.State):
    i: int = int (rx.LocalStorage(0))
    form_data: dict = {}
    levels = list(rx.LocalStorage(['-', '-', '-', '-', '-', '-', '-']))
    img_avl = 'img/no_image/no_tree.png'
    color = '#156082'
    list_color = ['#156082','#F6006F', '#F64000', '#00D25A', '#001468', '#AC0000', '#212121']

    async def handle_submit(self, form_data: dict) -> None:
        self.form_data = form_data
        
        if self.form_data['data'] != '':
            data = self.form_data['data']
            p, pad = T.search(data)
            if p is not None:
                try:
                    await self.delete_node(data)
                    if pad is None:
                        return rx.toast.info('La raíz no puede ser eliminada, presione el botón de reiniciar árbol.')
                    return rx.toast.success('Nodo eliminado.')
                except:
                    rx.toast.error('Error al eliminar el nodo, reintente.')
            else:
                try:
                    await self.insert_node(data)
                    return rx.toast.success('Nodo insertado.')
                except:
                    rx.toast.error('Error al insertar el nodo, reintente.')

    def levels_tour(self):
        if T.get_root() is not None:
            self.levels = ", ".join(T.levels_nr())

    async def insert_node(self, data: str):
        T.insert(data)
        await self.save_image()
        self.img_avl = f'img/tree_avl/image_avl{self.i}.png'
        self.i += 1

        image_avl(self.img_avl)
        self.levels_tour()
        rx.LocalStorage(T)

    async def delete_node(self, data: str):
        T.delete(data)
        await self.save_image()
        self.img_avl = f'img/tree_avl/image_avl{self.i}.png'
        self.i += 1

        image_avl(self.img_avl)
        self.levels_tour()
        rx.LocalStorage(T)

    async def change_color(self):
        if T.get_root() is not None:
            index_color = random.randint(0, len(self.list_color)-1)
            self.color = self.list_color[index_color]

            await self.save_image()
            self.img_avl = f'img/tree_avl/image_avl{self.i}.png'
            self.i += 1
            image_avl(self.img_avl)
            return rx.toast.success('Color cambiado.')
        else:
            return rx.toast.warning('No hay árbol para cambiar de color.')
    
    async def save_image(self):
        try:
            rmtree('assets/img/tree_avl') # Elimina la carpeta con las imágenes anteriores
        except:
            pass
        T.get_list_ady().plot(T.levels_nr(), self.color).render(f'assets/img/tree_avl/image_avl{self.i}', format='png', view=False, cleanup=True)
        image_path = f'.web/public/img/tree_avl/image_avl{self.i}.png'

        while not os.path.exists(image_path):
            await asyncio.sleep(0.1)
    
    def reset_tree(self):
        try:
            T.set_root(None)
            self.levels = ['-', '-', '-', '-', '-', '-', '-']
            self.img_avl = 'img/no_image/no_tree.png'
            rmtree('assets/img/tree_avl') # Elimina la carpeta con las imágenes anteriores
            return rx.toast.success(
                "El árbol ha sido barrido.", timeout=5000, close_on_click=True)
        except:
            return rx.toast.error(
                "No se pudo reiniciar el arbol, reintete.", timeout=5000, close_on_click=True)
        