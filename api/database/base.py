from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from ..config import settings

database_uri = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?sslmode={settings.DB_SSLMODE}"
engine = create_async_engine(
    database_uri, echo=False, pool_pre_ping=True, pool_size=10, max_overflow=0, pool_timeout=60
)
async_session = async_sessionmaker(engine, expire_on_commit=False, autocommit=False, autoflush=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


@asynccontextmanager
async def get_session_cm(in_transaction: bool = True) -> AsyncIterator[AsyncSession]:
    get_session_func = async_session if not in_transaction else async_session.begin
    async with get_session_func() as session:
        yield session