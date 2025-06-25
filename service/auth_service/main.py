import yaml
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pathlib import Path
from config.config import APP_CONFIG
from service.auth_service.routers.auth_service_routers import auth_service_router as auth_router
from service.utils.routers.health_router import health_router as health_router
from service.utils.routers.metrics_router import metrics_router as metrics_router

ROOT_DIR = Path(__file__).resolve().parents[2]


@asynccontextmanager
async def lifespan(service_app: FastAPI):
    openapi_schema = service_app.openapi()
    openapi_path = ROOT_DIR / 'docs/api/auth-service.yaml'
    with open(openapi_path, 'w') as file:
        yaml.dump(openapi_schema, file, allow_unicode=True, sort_keys=True)
    yield


app = FastAPI(
    title='Auth Service',
    description='Auth Service',
    version='1.0.0',
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth_router)
app.include_router(health_router)
app.include_router(metrics_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=APP_CONFIG.server_host,
        port=APP_CONFIG.server_port,
        reload=True,
    )
