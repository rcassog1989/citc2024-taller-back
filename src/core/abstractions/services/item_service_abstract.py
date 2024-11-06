from abc import ABC, abstractmethod
from src.core.models.item_domain import ItemDomain


class IItemService(ABC):

    @abstractmethod
    async def get_item_by_id(
        self,
        item_id: int
    ) -> ItemDomain:
        """Obtiene una item por su ID."""
        pass
