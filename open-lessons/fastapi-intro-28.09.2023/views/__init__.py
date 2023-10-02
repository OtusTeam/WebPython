__all__ = (
    "router_api_v1",
)

from fastapi import APIRouter

from .items import router as items_router
from .calc import router as calc_router

router_api_v1 = APIRouter(prefix="/api/v1")
router_api_v1.include_router(items_router)
router_api_v1.include_router(calc_router)
