from tienda.models.producto import Producto
from tienda.exceptions import ProductoNoEncontrado
 
class ProductoRepository:
    def __init__(self):
        self._datos = [
            Producto(1, "Laptop", 3500.00),
            Producto(2, "Mouse", 45.50),
            Producto(3, "Teclado", 120.00)
        ]
 
    def listar(self):
        return list(self._datos)
 
    def obtener(self, id):
        for p in self._datos:
            if p.id == id:
                return p
        raise ProductoNoEncontrado(f"No existe el producto {id}")
 
    def agregar(self, producto):
        nuevo_id = max([p.id for p in self._datos], default=0) + 1
        producto.id = nuevo_id
        self._datos.append(producto)
        return producto
