from pydantic import BaseModel


class ItemDomain(BaseModel):
    item_id: int = None
    item: str = None
