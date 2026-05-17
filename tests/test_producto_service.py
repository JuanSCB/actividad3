from tienda.services.producto_service import ProductoService


class RepoMock:

    def listar(self):
        return []

    def agregar(self, producto):
        return producto


def test_crear_producto():

    repo = RepoMock()

    service = ProductoService(repo)

    producto = service.crear_producto(
        "Monitor",
        500
    )

    assert producto.nombre == "Monitor"

    assert producto.precio == 500