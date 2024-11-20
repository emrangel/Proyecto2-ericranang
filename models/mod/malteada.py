from iproducto import IProducto

class Malteada(IProducto):
    def __init__(self, nombre:str, precio_publico:int, ingredientes:str, volumen:str):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.ingredientes = ingredientes
        self.volumen = volumen

    def calcular_costo(self):
        return sum(ingrediente.precio for ingrediente in self.ingredientes) + 500

    def calcular_calorias(self):
        total_calorias = sum(ingrediente.calorias for ingrediente in self.ingredientes)
        return total_calorias + 200

    def calcular_rentabilidad(self):
        costo = self.calcular_costo()
        return self.precio_publico - costo

    @property
    def tipo_vaso(self) -> str:
        """ Devuelve el valor del atributo privado 'tipo_vaso' """
        return self.__tipo_vaso
    
    @tipo_vaso.setter
    def tipo_vaso(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'tipo_vaso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__tipo_vaso = value
        else:
            raise ValueError('Expected str')
    @property
    def ingredientes(self) -> list:
        """ Devuelve el valor del atributo privado 'ingredientes' """
        return self.__ingredientes
    
    @ingredientes.setter
    def ingredientes(self, value:list) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ingredientes'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, list):
            self.__ingredientes = value
        else:
            raise ValueError('Expected list')
    @property
    def precio_publico(self) -> int:
        """ Devuelve el valor del atributo privado 'precio_publico' """
        return self.__precio_publico
    
    @precio_publico.setter
    def precio_publico(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'precio_publico'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__precio_publico = value
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