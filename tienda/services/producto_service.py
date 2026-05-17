from tienda.models.producto import Producto
from tienda.repositories.producto_repository import ProductoRepository
from tienda.exceptions import ErrorValidacion
 
class ProductoService:
    def __init__(self, repositorio=None):
        self._repo = repositorio or ProductoRepository()
 
    def listar_productos(self):
        return self._repo.listar()
 
    def crear_producto(self, nombre, precio):
        self._validar(nombre, precio)
        producto = Producto(id=0, nombre=nombre.strip(), precio=float(precio))
        return self._repo.agregar(producto)
 
    def _validar(self, nombre, precio):
        if not nombre or len(nombre.strip()) < 2:
            raise ErrorValidacion("El nombre debe tener al menos 2 caracteres.")
        try:
            precio_num = float(precio)
        except (TypeError, ValueError):
            raise ErrorValidacion("El precio debe ser un número.")
        if precio_num <= 0:
            raise ErrorValidacion("El precio debe ser mayor a cero.")
