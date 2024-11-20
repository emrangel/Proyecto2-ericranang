from abc import ABC, abstractmethod

class Ingrediente(ABC):
    def __init__(self, nombre:str, precio:int, calorias:int, inventario:float, es_vegetariano:bool) -> None:
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self.inventario = inventario
        self.es_vegetariano = es_vegetariano

    @abstractmethod
    def abastecer(self):
        pass

    @abstractmethod
    def descontar_inventario(self):
        pass

    def es_sano(self):
        return self.calorias < 100 or self.es_vegetariano

    @property
    def es_vegetariano(self) -> bool:
        """ Devuelve el valor del atributo privado 'es_vegetariano' """
        return self.__es_vegetariano
    
    @es_vegetariano.setter
    def es_vegetariano(self, value:bool) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'es_vegetariano'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, bool):
            self.__es_vegetariano = value
        else:
            raise ValueError('Expected bool')


    @property
    def inventario(self) -> float:
        """ Devuelve el valor del atributo privado 'inventario' """
        return self.__inventario

    @inventario.setter
    def inventario(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'inventario'
    
        Valida que el valor enviad  o corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self.__inventario = value   
        else:
            raise ValueError('Expected float')

    @property
    def calorias(self) -> int:
        """ Devuelve el valor del atributo privado 'calorias' """
        return self.__calorias
    

    @calorias.setter
    def calorias(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'calorias'
    
        Valida que el valor envi
        ado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__calorias = value

        else:
            raise ValueError('Expected int')
    
    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')

    @property
    def precio(self) -> int:
        """ Devuelve el valor del atributo privado 'precio' """
        return self.__precio
    
    @precio.setter
    def precio(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'precio'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__precio = value
        else:
            raise ValueError('Expected int')