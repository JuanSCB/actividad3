class ErrorValidacion(Exception):
    """Se lanza cuando los datos no cumplen las reglas del dominio."""
    pass
 
class ProductoNoEncontrado(Exception):
    """Se lanza cuando se busca un producto inexistente."""
    pass
