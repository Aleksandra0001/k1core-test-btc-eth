from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.database.base import get_session_cm
from api.database.models import Provider
from api.database.schemas import ProviderSchema

router = APIRouter()


@router.get("/providers", response_model=list[ProviderSchema])
async def get_providers(db: AsyncSession = Depends(get_session_cm)):
    """
    Получение списка всех провайдеров.
    """
    result = await db.execute(select(Provider))
    providers = result.scalars().all()
    return providers


@router.get("/providers/{provider_id}", response_model=ProviderSchema)
async def get_provider(provider_id: int, db: AsyncSession = Depends(get_session_cm)):
    """
    Получение информации о конкретном провайдере по ID.
    """
    provider = await db.get(Provider, provider_id)
    if not provider:
        return {"error": "Provider not found"}
    return provider