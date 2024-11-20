# funciones.py

# Punto 1: ¿Esto es Sano?
def es_sano(calorias: int, es_vegetariano: bool) -> bool:
    return calorias < 100 or es_vegetariano

# Punto 2: Calorías de un Producto
def contar_calorias(ingredientes_calorias: list[int]) -> float:
    total_calorias = sum(ingredientes_calorias) * 0.95
    return round(total_calorias, 2)

# Punto 3: Costos de un Producto
def calcular_costo(ingredientes: list[dict]) -> int:
    return sum(ingrediente['precio'] for ingrediente in ingredientes)

# Punto 4: Rentabilidad de un Producto
def calcular_rentabilidad(precio_venta: int, ingredientes: list[dict]) -> int:
    costo = calcular_costo(ingredientes)
    return precio_venta - costo


# Punto 5: Producto Más Rentable

def producto_mas_rentable(productos: list[dict]) -> str:
  producto_mas_rentable = None
  max_rentabilidad = 0.0

  for producto in productos:
    if producto["rentabilidad"] > max_rentabilidad:
      max_rentabilidad = producto["rentabilidad"]
      producto_mas_rentable = producto["nombre"]

  return producto_mas_rentable
