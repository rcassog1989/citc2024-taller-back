import pytest
from unittest.mock import AsyncMock

from src.core.abstractions.infrastructure.repository.item_repository_abstract import IItemRepository
from src.core.models.item_domain import ItemDomain
from src.core.services.item_service import ItemService

@pytest.mark.asyncio
async def test_get_item_by_id():
    mock_item_repository = AsyncMock(spec=IItemRepository)

    item_id = 1
    expected_item = ItemDomain(item_id=item_id, item="Test Item")
    mock_item_repository.get_item_by_id.return_value = expected_item

    item_service = ItemService(item_repository=mock_item_repository)

    result = await item_service.get_item_by_id(item_id)
    assert result == expected_item
    mock_item_repository.get_item_by_id.assert_awaited_once_with(item_id)
