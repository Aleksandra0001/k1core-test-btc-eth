from pydantic import BaseModel
from datetime import datetime

class CurrencySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ProviderSchema(BaseModel):
    id: int
    name: str
    api_key: str

    class Config:
        from_attributes = True

class BlockSchema(BaseModel):
    id: int
    block_number: int
    created_at: datetime
    stored_at: datetime
    currency: CurrencySchema
    provider: ProviderSchema

    class Config:
        from_attributes = True