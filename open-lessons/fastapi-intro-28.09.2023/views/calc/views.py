from typing import Annotated

from fastapi import APIRouter, Depends, Header

# from views.calc.schemas import CalcAction, ActionExtra
from .schemas import CalcAction, ActionExtra


router = APIRouter(prefix="/calc", tags=["Calc"])


@router.get("/add/")
def calc_add(params: CalcAction = Depends()):
    return {
        **params.model_dump(),
        "total": params.a + params.b,
    }


@router.post("/mul/")
# def calc_mul(params: Annotated[CalcAction, Body]):
def calc_mul(
    params: CalcAction,
    # action: str = Header(),
    # action: Annotated[str | None, Header()] = None,
    # action: Annotated[ActionExtra, Header()] = ActionExtra.TWO,
    # action: ActionExtra = Header(ActionExtra.ONE, alias="x-extra-action"),
    action: Annotated[ActionExtra, Header(alias="x-extra-action")] = ActionExtra.ONE,
):
    extra = 1
    if action is ActionExtra.TWO:
        extra = 2
    return {
        **params.model_dump(),
        "total": params.a * params.b * extra,
    }
