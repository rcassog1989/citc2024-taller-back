from abc import ABC, abstractmethod
from src.core.models.item_domain import itemDomain


class IitemService(ABC):

    @abstractmethod
    async def get_item_by_id(
        self,
        item_id: int
    ) -> itemDomain:
        """Obtiene una item por su ID."""
        pass
