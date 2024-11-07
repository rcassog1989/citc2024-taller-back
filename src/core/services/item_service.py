from src.core.abstractions.infrastructure.repository.item_repository_abstract import (
    IItemRepository)
from src.core.abstractions.services.item_service_abstract import IItemService
from src.core.models.item_domain import ItemDomain


class ItemService(IItemService):

    def __init__(self, item_repository: IItemRepository):
        self.item_repository = item_repository

    async def get_item_by_id(self, item_id: int) -> ItemDomain:
        return await self.item_repository.get_item_by_id(item_id)
