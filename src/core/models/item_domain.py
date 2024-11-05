from typing import Optional
from pydantic import BaseModel


class itemDomain(BaseModel):
    item_id: int = None
    item: str = None
