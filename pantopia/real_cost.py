from dataclasses import dataclass

@dataclass
class Externalities:
    carbon: float  # carbon footprint cost in dollars
    labor: float   # unethical labor penalty
    resources: float  # resource depletion cost
    waste: float  # waste management cost

    def total(self) -> float:
        return self.carbon + self.labor + self.resources + self.waste


def real_cost(base_price: float, ext: Externalities) -> float:
    """Calculate the real cost of a product."""
    return base_price + ext.total()
