from base import Base
from complemento import Complemento
from copa import Copa
from malteada import Malteada
from heladeria import Heladeria

# Crear algunos ingredientes para las pruebas
base_fresa = Base(nombre="Helado de Fresa", precio=1200, calorias=80, inventario=10.0, es_vegetariano=True, sabor="fresa")
complemento_chocolate = Complemento(nombre="Chispas de chocolate", precio=500, calorias=150, inventario=5.0, es_vegetariano=True)
complemento_mani = Complemento(nombre="Mani Japonés", precio=900, calorias=200, inventario=8.0, es_vegetariano=False)

# Crear productos con los ingredientes
copa_fresas = Copa(nombre="Copa de Fresas", precio_publico=7500, ingredientes=[base_fresa, complemento_chocolate, complemento_mani], tipo_vaso="grande")
copa_fresas2 = Copa(nombre="Copa de Fresas", precio_publico=7500, ingredientes=[base_fresa, complemento_chocolate, complemento_mani], tipo_vaso="grande")
malteada_choco = Malteada(nombre="Malteada Choco", precio_publico=8000, ingredientes=[base_fresa, complemento_chocolate, complemento_mani], volumen=12)
malteada_choco2 = Malteada(nombre="Malteada Choco", precio_publico=8000, ingredientes=[base_fresa, complemento_chocolate, complemento_mani], volumen=12)
malteada_choco3 = Malteada(nombre="Malteada Choco", precio_publico=8000, ingredientes=[base_fresa, complemento_chocolate, complemento_mani], volumen=12)

# Instanciar la heladería con los productos
# heladeria = Heladeria(productos=[copa_fresas, malteada_choco])

heladeria = Heladeria(
    productos=[
        copa_fresas,
        copa_fresas2,
        malteada_choco
                      ])

# Menú de opciones
def mostrar_menu():
    print("\n--- Menú de Heladería ---")
    print("1. Vender Producto")
    print("2. Abastecer Ingrediente")
    print("3. Renovar Inventario de Complemento")
    print("4. Ver Producto Más Rentable")
    print("5. Mostrar Inventario de Ingredientes")
    print("6. Mostrar Ventas del Día")
    print("7. Salir")

def vender_producto():
    nombre = input("Ingrese el nombre del producto a vender: ")
    if heladeria.vender(nombre):
        print(f"El producto '{nombre}' se ha vendido con éxito.")
    else:
        print(f"No hay suficiente inventario para vender '{nombre}'.")

def abastecer_ingrediente():
    nombre = input("Ingrese el nombre del ingrediente a abastecer: ")
    if nombre == base_fresa.nombre:
        base_fresa.abastecer()
        print(f"Se han abastecido unidades de '{nombre}'. Nuevo inventario: {base_fresa.inventario}")
    elif nombre == complemento_chocolate.nombre:
        complemento_chocolate.abastecer()
        print(f"Se han abastecido unidades de '{nombre}'. Nuevo inventario: {complemento_chocolate.inventario}")
    elif nombre == complemento_mani.nombre:
        complemento_mani.abastecer()
        print(f"Se han abastecido unidades de '{nombre}'. Nuevo inventario: {complemento_mani.inventario}")
    else:
        print("Ingrediente no encontrado.")

def renovar_inventario_complemento():
    nombre = input("Ingrese el nombre del complemento a renovar: ")
    if nombre == complemento_chocolate.nombre:
        complemento_chocolate.renovar_inventario()
        print(f"El inventario de '{nombre}' ha sido renovado a 0.")
    elif nombre == complemento_mani.nombre:
        complemento_mani.renovar_inventario()
        print(f"El inventario de '{nombre}' ha sido renovado a 0.")
    else:
        print("Complemento no encontrado o no es un complemento.")

def producto_mas_rentable():
    producto = heladeria.producto_mas_rentable()
    print(f"El producto más rentable es '{producto.nombre}' con una rentabilidad de {producto.calcular_rentabilidad()}.")

def mostrar_inventario_ingredientes():
    print(f"\nInventario:")
    print(f"{base_fresa.nombre}: {base_fresa.inventario} unidades")
    print(f"{complemento_chocolate.nombre}: {complemento_chocolate.inventario} unidades")
    print(f"{complemento_mani.nombre}: {complemento_mani.inventario} unidades")

def mostrar_ventas_del_dia():
    print(f"Las ventas del día son: {heladeria.ventas_del_dia}")

# Loop principal del menú
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        vender_producto()
    elif opcion == "2":
        abastecer_ingrediente()
    elif opcion == "3":
        renovar_inventario_complemento()
    elif opcion == "4":
        producto_mas_rentable()
    elif opcion == "5":
        mostrar_inventario_ingredientes()
    elif opcion == "6":
        mostrar_ventas_del_dia()
    elif opcion == "7":
        print("Gracias por usar el sistema de la heladería. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
