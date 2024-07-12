from typing import List, Any, Optional
import os
from PIL import Image

import graphviz as gv

class GraphList:
    def __init__(self) -> None:
        self.__n = 0
        self.__list_ady: List[List[Any]] = []
    
    def get_list_ady(self) -> List[List[Any]]:
        return self.__list_ady
    
    def add_vertex(self, size) -> None:
        for i in range(size):
            self.__list_ady.append([])
            self.__n += 1
    
    def add_edge(self, lista_level: List[Any], vi, vf) -> bool:
        self.__list_ady[lista_level.index(vi)].append(vf)
        return True
    
    def search_image(self,name_file: str) -> str:
        carpeta = 'assets/Data'
        directorio_actual = os.path.abspath(carpeta)
        for imagenes in os.listdir(carpeta):
            path = os.path.join(directorio_actual, imagenes)
            imagenes_name = imagenes.split('.')
            if len(imagenes_name) > 2:
                imagenes_name = f'{imagenes_name[0]}.{imagenes_name[1]}'
            else:
                imagenes_name = imagenes_name[0]
            if imagenes_name == name_file:
                Format = imagenes.split('.')[-1]
                if(Format == 'bmp'):
                    bmp_path = path
                    imagen_bmp = Image.open(bmp_path)
                    png_path = path
                    png_path = png_path.replace('bmp', 'png')
                    imagen_bmp.save(png_path, "PNG")
                    os.remove(bmp_path)
                    path = png_path
                    return path
                elif(Format == 'jpg'):
                    bmp_path = path
                    imagen_bmp = Image.open(bmp_path)
                    png_path = path
                    png_path = png_path.replace('jpg', 'png')
                    imagen_bmp.save(png_path, "PNG")
                    os.remove(bmp_path)
                    path = png_path
                    return path
                else:
                    return path
        return None
    
    def plot(self, list_level: List['str']) -> 'gv.Digraph':
        g = gv.Digraph(format='png')
        for i in range(self.__n):
            g.node(str(i), str(list_level[i]), shape='circle', style='filled', fillcolor='#156082', color='#156082', fontcolor='white', fontsize='20', width='0.7', height='0.7', fontname='Comic Sans MS')
        for i in range(len(list_level)):
            for j in self.__list_ady[i]:
                g.edge(str(i), str(list_level.index(j)), color='#156082', penwidth='1.0', width='0.5', height='0.5', style='solid', arrowhead='vee', arrowsize='0.5')
        return g


