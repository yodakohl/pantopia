from dataclasses import dataclass, field
from uuid import uuid4

from .real_cost import Externalities

@dataclass
class Product:
    """Representation of a product with global SKU."""

    name: str
    price: float
    externalities: Externalities
    description: str = ""
    origin: str = ""
    sku: str = field(default_factory=lambda: str(uuid4()))

    @staticmethod
    def from_dict(data: dict) -> "Product":
        sku = data.get("sku") or str(uuid4())
        ext_data = data.get("externalities", {})
        ext = Externalities(**ext_data)
        return Product(
            name=data.get("name", ""),
            price=data.get("price", 0.0),
            externalities=ext,
            description=data.get("description", ""),
            origin=data.get("origin", ""),
            sku=sku,
        )
