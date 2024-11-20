class Heladeria:
    def __init__(self, productos:list) -> None:
        self.productos = productos
        self.ventas_del_dia = 0


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

    # def vender(self, nombre_producto):
    #     for producto in self.productos:
    #         if producto.nombre == nombre_producto:
    #             # Verificar si hay suficiente inventario para cada ingrediente usando su método de descontar
    #             suficiente_inventario = True
    #             for ingrediente in producto.ingredientes:
    #                 if isinstance(ingrediente, Base) and ingrediente.inventario < 0.2:
    #                     suficiente_inventario = False
    #                 elif isinstance(ingrediente, Complemento) and ingrediente.inventario < 1:
    #                     suficiente_inventario = False

    #             # Si hay suficiente inventario, aplicar el descuento de inventario usando el método descontar
    #             if suficiente_inventario:
    #                 for ingrediente in producto.ingredientes:
    #                     ingrediente.descontar()  # Descontar según el tipo de ingrediente

    #                 # Sumar el precio del producto a las ventas del día
    #                 self.ventas_del_dia += producto.precio_publico
    #                 print(f"El producto '{nombre_producto}' se ha vendido con éxito.")
    #                 return True
    #             else:
    #                 print(f"No hay suficiente inventario para vender '{nombre_producto}'.")
    #                 return False

    #     print(f"Producto '{nombre_producto}' no encontrado.")
    #     return False
