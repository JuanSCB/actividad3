from dataclasses import dataclass
 
@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
 
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "precio": self.precio}
