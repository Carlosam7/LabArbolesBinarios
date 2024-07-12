from typing import List, Optional, Any

from LabArbolesBinarios.classes.Node import Node
from LabArbolesBinarios.classes.GraphList import GraphList


class Avl:
    def __init__(self, root: 'Node') -> None:
        self.__root = root
        self.__list_ady: Optional['GraphList'] = [[]]
        
        self.set_list_ady()
    
    def get_root(self) -> 'Node':
        return self.__root
    def set_root(self, root: 'Node') -> None:
        self.__root = root
    
    def get_height(self, node: 'Node') -> int: # height of the tree (number of levels)
        if node is None:
            return 0
        return max(self.get_height(node.get_left()), self.get_height(node.get_right())) + 1
    
    def get_size(self, node:'Node'): # Size of the tree (number of nodes)
      if node is None:
        return 0
      else:
        return self.get_size(node.get_left()) + 1 + self.get_size(node.get_right())
      
    # SEARCH, INSERT, DELETE
    def search(self, data: 'str'): # Search
        p, pad = self.get_root(), None
        while p is not None:
            if data == p.get_data():
                return p, pad
            elif data < p.get_data():
                pad = p
                p = p.get_left()
            else:
                pad = p
                p = p.get_right()
        return p, pad

    def insert(self, data: 'Any') -> bool: # Insert
        root = self.get_root()
        to_insert = Node(data)
        if root == None:
            root = to_insert
            self.set_list_ady()
            return True
        else:
            p, pad = self.search(data)
            if p != None:
                return False
            elif data < pad.get_data():
                pad.set_left(to_insert)
            else:
                pad.set_right(to_insert)

            self.rebalance()
            self.set_list_ady()
            return True
    
    # Functions for delete 
    def pred(self, node: 'Node'): # Predecesor (Node with the greatest value less than the node)
        p, pad = node.get_left(), node
        while p.get_right() is not None:
            pad = p
            p = p.get_right()
        return p, pad
    
    def delete(self, data: 'str') -> bool: # Delete a node from the tree
        p, pad = self.search(data)
        if p is not None:
            if p.get_left() is None and p.get_right() is None:
                if p == pad.get_left():
                    pad.set_left(None)
                else:
                    pad.set_right(None)

            elif p.get_left() is not None and p.get_right() is None:
                if pad != None:
                    if p == pad.get_left():
                        pad.set_left(p.get_left())
                    else:
                        pad.set_right(p.get_left())
            
            elif p.get_left() == None and p.get_right() != None:
                if p == pad.get_left():
                    pad.set_left(p.get_right())
                else:
                    pad.set_right(p.get_right())
            else:
                pred, pad_pred = self.pred(p)
                p.set_data(pred.get_data())
                if pred.get_left() is not None:
                    if pad_pred == p:
                        pad_pred.set_left(pred.get_left())
                    else:
                        pad_pred.set_right(pred.get_left())
                else:
                    if pad_pred == p:
                        pad_pred.set_left(None)
                    else:
                        pad_pred.set_right(None)
                del pred
            self.rebalance()
            self.set_list_ady()
            return True
        return False

    
    def get_list_ady(self) -> 'GraphList':
        return self.__list_ady
    
    def set_list_ady(self) -> None:
        self.__list_ady = GraphList()
        self.__list_ady.add_vertex(self.get_size(self.get_root()))
        
        p = self.get_root()
        q: List['Node'] = []
        q.append(p)
        while not len(q) == 0:
            p = q.pop(0)
            son, pad_node = self.search(p.get_data())
            pad = pad_node.get_data() if pad_node is not None else None
            if p.get_left() is not None:
                q.append(p.get_left())
            if p.get_right() is not None:
                q.append(p.get_right())
            if p is not None and pad is not None:
                self.__list_ady.add_edge(self.levels_nr(), pad, p.get_data())
    
    # TRAVERSALS
    def postorder(self) -> 'List': # Postorder Traversal (Left, Right, Root)
        p = self.get_root()
        s: List['Node'] = []
        s_data: List['str'] = []
        s.append(p)
        while len(s) != 0:
            p = s.pop()
            s_data.append(p.get_data())
            if p.get_left() is not None:
                s.append(p.get_left())
            if p.get_right() is not None:
                s.append(p.get_right())
        
        return s_data
    
    def list_level(self, node: "Node", n, lista: List['Any']): # List of nodes in a level n of the tree (root is level 0)
        if node != None:
            if n == 0:
                return lista.append(node.get_data())
            self.list_level(node.get_left(), n-1, lista)
            self.list_level(node.get_right(), n-1, lista)
    
    def levels_nr(self) -> List['Any']: # List of nodes in the tree by levels (root is level 0) (Non-Recursive)
        p = self.get_root()
        q: List['Node'] = []
        q.append(p)
        lista = []
        while not len(q) == 0:
            p = q.pop(0)
            lista.append(p.get_data())
            if p.get_left() is not None:
                q.append(p.get_left())
            if p.get_right() is not None:
                q.append(p.get_right())
        return lista
    
    def level_node(self, data: 'str'): # Level of a node in the tree (root is level 0) (Non-Recursive)
        cont = 0
        p = self.get_root()
        while (p != None):
            if p.get_data() == data:
                return cont
            elif data < p.get_data():
                p = p.get_left()
                cont += 1
            else:
                p = p.get_right()
                cont += 1
        return cont

    # ROTATIONS AND REBALANCE FUNCTIONS
    def get_balance(self, elem: str) -> Optional[int]: # Balance Factor of a node (Height of the right subtree - Height of the left subtree)
        node, pad = self.search(elem)
        if node is None:
            return False
        return self.get_height(node.get_right()) - self.get_height(node.get_left())
    
    def rotate_right(self, data: 'Node') -> 'Node': # Right Rotation
        node, pad = self.search(data)
        temp = node.get_left()
        node.set_left(temp.get_right())
        temp.set_right(node)
        if node == self.__root:
          self.set_root(temp)
        elif node.get_data() > pad.get_data():
          pad.set_right(temp)
        else:
          pad.set_left(temp)
        self.set_list_ady()
        return temp
    
    def rotate_left(self, data: 'str') -> 'Node': # Left Rotation
        node, pad = self.search(data)
        temp = node.get_right()
        node.set_right(temp.get_left())
        temp.set_left(node)
        if node == self.get_root():
          self.set_root(temp)
        elif node.get_data() > pad.get_data():
          pad.set_right(temp)
        else:
          pad.set_left(temp)
        self.set_list_ady()
        return temp
    
    def rotate_left_right(self, data: 'str') -> 'Node': # Left-Right Rotation
        node, pad = self.search(data)
        self.rotate_left(node.get_left().get_data())
        return self.rotate_right(node.get_data())
    
    
    def rotate_right_left(self, data: 'str') -> 'Node':
        node, pad = self.search(data)
        self.rotate_right(node.get_right().get_data())
        return self.rotate_left(data)


    def rebalance(self) -> None: # Rebalance the tree after an insertion or deletion
        lista = self.levels_nr()
        lista.reverse()
        for data in lista:
            node, pad = self.search(data)
            fact_balance = self.get_balance(data)
            if fact_balance == 2:
                if self.get_balance(node.get_right().get_data()) == 1:
                    self.rotate_left(data)
                elif self.get_balance(node.get_right().get_data()) == 0:
                    self.rotate_left(data)
                else:
                    self.rotate_right_left(data)
            
            elif fact_balance == -2:
                if self.get_balance(node.get_left().get_data()) == -1:
                    self.rotate_right(data)
                else:
                    self.rotate_left_right(data)
            else:
                pass


# T = Avl(Node('0001'))
# T.insert('carsgraz_001')
# T.insert('horse-17')
# T.insert('horse-18')
# T.insert('rider-8')
# T.insert('rider-20')
# T.insert('cat.8')
# T.insert('dog.27')
# T.insert('dog.29')
# T.insert('dog.120')
# T.insert('0210')
# T.insert('bike_024')
# T.insert('bike_180')
# T.insert('cargraz_164')
# T.insert('cat.154')
# T.insert('horse-33')
# T.insert('horse-40')
# T.insert('rider-44')
# T.insert('rider-197')
# print(T.get_list_ady().get_list_ady())
# print()

# print(T.levels_nr())
# lista = []
# T.list_level(T.get_root(), 3, lista)
# print(lista)
# print()
# print(T.get_list_ady().search_image('rider-44'))

# T.get_list_ady().plot(T.levels_nr()).render('assets/img/tree_avl/image_avl', format='png', view=True, cleanup=True)
# Plot the tree and save it as an image file in the assets/img/tree_avl folder of the project directory (LabArbolesBinarios)

