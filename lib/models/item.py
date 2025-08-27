# lib/models/item.py
from sqlalchemy import Column, Integer, String, Float
from . import Base  # import Base from __init__.py

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Item {self.id}: {self.name} ({self.category}) - {self.quantity} in stock @ Ksh {self.price}>"
