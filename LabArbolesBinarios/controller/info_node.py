import reflex as rx
from typing import Optional

from LabArbolesBinarios.controller.class_tree import T

class InfoNode(rx.State):
    data = ''
    src = 'img/no_image/no_image.png'
    categoria = ''
    peso = ''
    nivel = ''
    factor_equilibrio = ''
    padre = ''
    abuelo = ''

    def set_data(self, data: str):
        self.data = data
        self.get_info()

    def get_info(self):
        if T.get_root() is not None:
            p, pad = T.search(self.data)
            if p is not None:
                self.src = self.image(self.data)
                self.categoria = self.type(self.data)
                self.peso = self.size(self.data)
                self.nivel = self.level(self.data)
                self.factor_equilibrio = self.balance_factor(self.data)
                self.padre = self.father(self.data)
                self.abuelo = self.grandfather(self.data)

    def image(self, data: str):
        try:
            return T.get_list_ady().search_image(data).replace('\\','/').partition('assets/')[-1]
        except:
            return 'img/no_image/no_image.png'

    def type(self, data: str):
        type = None
        if T.get_list_ady().search_image(data) != None:
            if(data.split('0')[0] == ''):
                type = 'flowers'
            elif(data.split('_')[0] == 'carsgraz'):
                type = 'cars'
            elif(data.split('.')[0] == 'cat'):
                type = 'cats'
            elif(data.split('-')[0] == 'rider'):
                type = 'human'
            elif(data.split('.')[0] == 'dog'):
                type = 'dogs'
            elif(data.split('-')[0] == 'horse'):
                type = 'horses'
            elif(data.split('_')[0] == 'bike'):
                type = 'bike'
        return type
    
    def size(self, data: str) -> int:
        node, pad = T.search(data)
        if node is not None:
            return node.get_size()
        return 0
    
    def level(self, data: str) -> Optional[int]:
        node, pad = T.search(data)
        if node is not None:
            return T.level_node(data)
        return None
    
    def balance_factor(self, data: str) -> Optional[int]:
        return T.get_balance(data)
        
    
    def father(self, data: str) -> Optional[str]:
        node, pad = T.search(data)
        if node is not None:
            if pad is not None:
                return pad.get_data()
        return 'Sin padre'
    
    def grandfather(self, data: str) -> Optional[str]:
        node, pad = T.search(data)
        if pad is not None:
            pad, grandpa = T.search(pad.get_data())
            if grandpa is not None:
                return grandpa.get_data()
        return 'Sin abuelo'
