import json

from tienda.models.producto import Producto
from tienda.exceptions import ProductoNoEncontrado


class ProductoRepository:

    def __init__(self):

        self.archivo = "productos.json"


    def _leer(self):

        try:

            with open(self.archivo, "r") as f:

                datos = json.load(f)

                return [Producto(**p) for p in datos]

        except FileNotFoundError:

            return []


    def _guardar(self, productos):

        with open(self.archivo, "w") as f:

            json.dump(
                [p.to_dict() for p in productos],
                f,
                indent=4
            )


    def listar(self):

        return self._leer()


    def obtener(self, id):

        productos = self._leer()

        for p in productos:

            if p.id == id:
                return p

        raise ProductoNoEncontrado(
            f"No existe el producto {id}"
        )


    def agregar(self, producto):

        productos = self._leer()

        nuevo_id = max(
            [p.id for p in productos],
            default=0
        ) + 1

        producto.id = nuevo_id

        productos.append(producto)

        self._guardar(productos)

        return producto


    def actualizar(self, id, nombre, precio):

        productos = self._leer()

        for p in productos:

            if p.id == id:

                p.nombre = nombre

                p.precio = precio

                self._guardar(productos)

                return p

        raise ProductoNoEncontrado(
            f"No existe el producto {id}"
        )


    def eliminar(self, id):

        productos = self._leer()

        for p in productos:

            if p.id == id:

                productos.remove(p)

                self._guardar(productos)

                return

        raise ProductoNoEncontrado(
            f"No existe el producto {id}"
        )