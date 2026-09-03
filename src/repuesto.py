class Repuesto:
    def __init__(self, codigo: str, nombre: str, marca: str, precio: float, stock: int):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock

class InventarioService:
    def __init__(self):
        self._almacen = {}

    def registrar_repuesto(self, repuesto: Repuesto):
        self._almacen[repuesto.codigo] = repuesto
        return True

    def buscar_por_codigo(self, codigo: str):
        return self._almacen.get(codigo, None)