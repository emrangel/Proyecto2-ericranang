from models.ingrediente import Ingrediente
from models.producto import Producto
from funciones import *

class Heladeria:
    def __init__(self, productos:list = [], ingredientes:list = []) -> None:
        self.productos = productos
        self.ingredientes = ingredientes
        self.ventas_del_dia = 0

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
    def productos(self) -> list:
        """ Devuelve el valor del atributo privado 'productos' """
        return self.__productos
    
    @productos.setter
    def productos(self, value:list) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'productos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, list):
            self.__productos = value
        elif len(value)!=4:
            raise ValueError('Mayor a 4 productos')
        else:
            raise ValueError('Expected str')    
    
    # Método que calcula el producto más rentable
    def obtener_producto_mas_rentable(self):
        lista = []
        for producto in self.productos:
             lista.append({"nombre": producto.nombre, "rentabilidad": producto.calcular_rentabilidad()})
        return producto_mas_rentable(lista)

    def producto_mas_rentable(productos: list[dict]) -> str:
        producto_mas_rentable = None
        max_rentabilidad = 0.0

        for producto in productos:
            if producto["rentabilidad"] > max_rentabilidad:
                max_rentabilidad = producto["rentabilidad"]
                producto_mas_rentable = producto["nombre"]

        return producto_mas_rentable


    def vender(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if all(ingrediente.inventario >= 1 for ingrediente in producto.ingredientes):
                    for ingrediente in producto.ingredientes:
                        ingrediente.descontar_inventario()
                    self.ventas_del_dia += producto.precio_publico
                    return True
        return False
    
    def descontar_inventario(self, producto):
        for ingrediente in producto.ingredientes:
            if ingrediente.tipo == 'Complemento':
                ingrediente.inventario = ingrediente.inventario
            elif ingrediente.tipo == 'Base': # ingrediente base
                ingrediente.inventario = ingrediente.inventario

    # Método que renueva el inventario de ingredientes a 0 (solo aplica para complementos)
    def renovar_inventario(self):
        for ingrediente in self.ingredientes:
            if ingrediente.tipo == 'Complemento':
                ingrediente.renovar_inventario()

    # Método que permite renovar el inventario de ingredientes
    def abastecer_inventario(self):
        for ingrediente in self.ingredientes:
            ingrediente.abastecer()

    # Método que permite agregar un ingrediente al sistema, validando que el tipo sea correcto
    def agregar_ingrediente(self, ingrediente: Ingrediente):
        if isinstance(ingrediente, Ingrediente):
            self._ingredientes.append(ingrediente)
        else:
            raise ValueError('Expected Ingrediente')

    # Método que permite agregar un producto al sistema,validando que el tipo sea correcto
    def agregar_producto(self, producto: Producto):
        if isinstance(producto, Producto):
            self._productos.append(producto)
            for ingrediente in producto.ingredientes:
                if not ingrediente in self._ingredientes:
                    self.ingredientes.append(ingrediente)
        else:
            raise ValueError('Expected Producto')

     #Método que determina si un ingrediente es sano
    def ingrediente_es_sano(ingrediente: Ingrediente) -> bool:
        if not isinstance(ingrediente, Ingrediente):
            raise ValueError("El ingrediente no es del tipo esperado")
        return ingrediente.es_sano()