from typing import Annotated

from fastapi import APIRouter, Path

from .schemas import Item

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def get_items():
    return {
        "data": [
            {
                "id": 1,
                "name": "item_1",
            },
            {
                "id": 2,
                "name": "item_2",
            },
        ]
    }


@router.post("/")
def create_item(item: Item):
    return {
        "data": {
            "id": 0,
            "attributes": item,
        },
    }


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=100_000)]):
    # response = requests.get('api.json')
    return {
        "data": {
            "id": item_id,
            "name": f"item_{item_id}",
        },
    }
