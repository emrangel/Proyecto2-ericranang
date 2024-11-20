from ingrediente import Ingrediente

class Complemento(Ingrediente):
    def __init__(self, nombre:str, precio:int, calorias:int, inventario:float, es_vegetariano:bool) -> None:
       super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
        
    def abastecer(self):
        self.inventario += 10

    def descontar_inventario(self):
        self.inventario -=1

    def renovar_inventario(self):
        self.inventario = 0.0
