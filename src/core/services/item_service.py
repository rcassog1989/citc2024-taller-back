from src.core.abstractions.infrastructure.repository.item_repository_abstract import IitemRepository
from src.core.abstractions.services.item_service_abstract import IitemService
from src.core.models.item_domain import itemDomain

class itemService(IitemService):

    def __init__(self, item_repository: IitemRepository):
        self.item_repository = item_repository

    async def get_item_by_id(self, item_id: int) -> itemDomain:
        return await self.item_repository.get_item_by_id(item_id)
