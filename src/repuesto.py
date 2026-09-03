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
