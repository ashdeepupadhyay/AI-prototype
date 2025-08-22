from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True  # For Pydantic v2, replaces orm_mode        from pydantic import BaseModel
        from typing import Optional
        
        class ItemBase(BaseModel):
            name: str
            description: Optional[str] = None
        
        class ItemCreate(ItemBase):
            pass
        
        class ItemUpdate(ItemBase):
            pass
        
        class Item(ItemBase):
            id: int
        
            class Config:
                from_attributes = True  # For Pydantic v2, replaces orm_modefrom pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemList(BaseModel):
    items: List[Item]