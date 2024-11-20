from ingrediente import Ingrediente

class Base(Ingrediente):
    def __init__(self, nombre:str, precio:int, calorias:int, inventario:float, es_vegetariano:bool, sabor:str) -> None:
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
        self.sabor = sabor

    def abastecer(self):
        self.inventario += 5
    
    def descontar_inventario(self):
        self.inventario -=0.2

    @property
    def sabor(self) -> str:
        """ Devuelve el valor del atributo privado 'sabor' """
        return self.__sabor
    
    @sabor.setter
    def sabor(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'sabor'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__sabor = value
        else:
            raise ValueError('Expected str')
