from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from api.routers.blocks import router as block
from api.routers.currencies import router as currency
from api.routers.providers import router as provider


app = FastAPI(title="K1CORE LTD - Blockchain API")

# Подключаем маршруты
app.include_router(block, prefix="/api", tags=["Blocks"])
app.include_router(currency, prefix="/api", tags=["Currencies"])
app.include_router(provider, prefix="/api", tags=["Providers"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )


@app.get("/health_check")
async def health_check():
    return ORJSONResponse(content={"status": "ok"})