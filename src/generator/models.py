from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from test import log_all_methods
import enum

@dataclass
class Product(frozen=True, slots = True):
    product_id: int
    name: str
    category: ProductCategory
    price: float

@dataclass
class Customer(frozen=True, slots = True):
    customer_id: int
    name: str
    city: str

@dataclass    
class Order(frozen=True, slots = True):
    order_id: int
    timestamp: datetime
    customer_id: int
    product_id: int
    qantity: int
    total_amount: float
    payment_method: PaymentMethod
    status: OrderStatus
    is_anomaly: bool = False

class OrderStatus(enum.StrEnum):
    CREATED = "created"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class PaymentMethod(enum.StrEnum):
    CARD = "card"
    CASH = "cash"
    SBP = "sbp"

class ProductCategory(enum.StrEnum):
    ELECTRONICS = "electronics"
    CLOTHING = "clothings"
    BOOKS = "books"
    HOME = "home"