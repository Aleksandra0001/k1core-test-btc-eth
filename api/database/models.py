from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

Base = declarative_base()


class Currency(Base):
    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    blocks: Mapped[list["Block"]] = relationship(back_populates="currency")


class Provider(Base):
    __tablename__ = "providers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    api_key: Mapped[str] = mapped_column(String(255), nullable=False)

    blocks: Mapped[list["Block"]] = relationship(back_populates="provider")


class Block(Base):
    __tablename__ = "blocks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    currency_id: Mapped[int] = mapped_column(ForeignKey("currencies.id"))
    provider_id: Mapped[int] = mapped_column(ForeignKey("providers.id"))

    block_number: Mapped[int] = mapped_column(Integer, unique=True, nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    stored_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    currency: Mapped["Currency"] = relationship(back_populates="blocks")
    provider: Mapped["Provider"] = relationship(back_populates="blocks")