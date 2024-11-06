from src.core.abstractions.infrastructure.repository.item_repository_abstract import IItemRepository
from src.core.models.item_domain import ItemDomain

class ItemRepository(IItemRepository):
    def __init__(self):
        pass

    async def get_item_by_id(self, item_id: int) -> ItemDomain:
        self.fake_data = [
            {"item_id": 1, "item": "Item A"},
            {"item_id": 2, "item": "Item B"},
            {"item_id": 3, "item": "Item C"}
        ]
        row = next((row for row in self.fake_data if row["item_id"] == item_id), None)
        if row:
            return ItemDomain(
                item_id=row["item_id"],
                item=row["item"]
            )
        return None
