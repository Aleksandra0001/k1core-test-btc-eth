from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.database.base import get_session_cm
from api.database.models import Block
from api.database.schemas import BlockSchema

router = APIRouter()


@router.get("/blocks", response_model=list[BlockSchema])
async def get_blocks(db: AsyncSession = Depends(get_session_cm)):
    """
    Получение списка всех блоков.
    """
    result = await db.execute(select(Block))
    blocks = result.scalars().all()
    return blocks


@router.get("/blocks/{block_id}", response_model=BlockSchema)
async def get_block(block_id: int, db: AsyncSession = Depends(get_session_cm)):
    """
    Получение информации о конкретном блоке по его ID.
    """
    block = await db.get(Block, block_id)
    if not block:
        return {"error": "Block not found"}
    return block