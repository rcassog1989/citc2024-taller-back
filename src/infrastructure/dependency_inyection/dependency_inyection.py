
from src.core.services.item_service import ItemService
from src.infrastructure.repository.Item_repository import ItemRepository

def build_item_service():
    return ItemRepository()
