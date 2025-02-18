from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.database.base import get_session_cm
from api.database.models import Currency
from api.database.schemas import CurrencySchema

router = APIRouter()


@router.get("/currencies", response_model=list[CurrencySchema])
async def get_currencies(db: AsyncSession = Depends(get_session_cm)):
    """
    Получение списка всех валют.
    """
    result = await db.execute(select(Currency))
    currencies = result.scalars().all()
    return currencies


@router.get("/currencies/{currency_id}", response_model=CurrencySchema)
async def get_currency(currency_id: int, db: AsyncSession = Depends(get_session_cm)):
    """
    Получение информации о конкретной валюте по ID.
    """
    currency = await db.get(Currency, currency_id)
    if not currency:
        return {"error": "Currency not found"}
    return currency