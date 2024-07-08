from typing import Optional, Any
from GraphList import GraphList
import os

class Node:
    def __init__(self, data:'str') -> None:
        self.__left: Optional['Node'] = None
        self.__right: Optional['Node'] = None
        self.__data = data #Nombre de la imagen SIN extensión

        self.__size = self.set_size(data)
        
        
    
    def get_left(self) -> 'Node':
        return self.__left
    def set_left(self, left: 'Node') -> None:
        self.__left = left
    
    def get_right(self) -> 'Node':
        return self.__right
    def set_right(self, right: 'Node') -> None:
        self.__right = right
    
    def get_data(self) -> 'str':
        return self.__data
    def set_data(self, data: 'str') -> None:
        self.__data = data
    
    def get_size(self) -> 'Any':
        return self.__size
    def set_size(self, name:str):
        size = 0
        imagen = GraphList.search_image(GraphList,name)
        if(imagen != None):
            name_file = str(os.path.basename(imagen))
            size = str(os.path.getsize(imagen))
            if size == 0:
                size = 'No se encontro el tamaño'
            else:
                size = size
        return size
    
    def set_type(self, name:str) -> None:
        type = None
        
        if(name.split('0')[0] == ''):
            type = 'flowers'
        elif(name.split('_')[0] == 'carsgraz'):
            type = 'cars'
        elif(name.split('.')[0] == 'cat'):
            type = 'cats'
        elif(name.split('-')[0] == 'rider'):
            type = 'human'
        elif(name.split('.')[0] == 'dog'):
            type = 'dogs'
        elif(name.split('-')[0] == 'horse'):
            type = 'horses'
        elif(name.split('_')[0] == 'bike'):
            type = 'bike'
        
        return type


# nodo = Node('horse-195')
# print(nodo.get_data())
# print(nodo.get_size())
# print(nodo.set_type(nodo.get_data()))

# print()

# nodo = Node('0028')
# print(nodo.get_data())
# print(nodo.get_size())
# print(nodo.set_type(nodo.get_data()))

# print()


# nodo = Node('rider-7')
# print(nodo.get_data())
# print(nodo.get_size())
# print(nodo.set_type(nodo.get_data()))

# print()


# nodo = Node('dog-195')
# print(nodo.get_data())
# print(nodo.get_size())
# print(nodo.set_type(nodo.get_data()))

# print()


# nodo = Node('cat.177')
# print(nodo.get_data())
# print(nodo.get_size())
# print(nodo.set_type(nodo.get_data()))

# print()


# nodo = Node('carsgraz_397')
# print(nodo.get_data())
# print(nodo.get_size())
# print(nodo.set_type(nodo.get_data()))