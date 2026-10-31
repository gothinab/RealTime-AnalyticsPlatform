from __future__ import annotations

import enum
import random


class AnomalyKind(enum.StrEnum):
    BULK_ORDER = "bulk_order"
    PRICE_ERROR = "price_error"
    HIGHT_VALUE_ORDER = "hight_value_order"
    NIGHT_ORDER = "night_order"

"random = random.Random(seed)"

class AnomalyPolicy:
    def __init__(self, probability: float, strength: float):
        ...
    
    @property
    def strength(self) -> float:
        return self._strength
    
    def decide(self) -> AnomalyKind | None:
        if self._rng.random() >= self._probability:
            return None
        return self._rng.choice(list(AnomalyKind))