
from fastapi import Depends
from src.core.services.item_service import itemService

def build_item_service():
    return itemService()
