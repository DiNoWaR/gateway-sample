from fastapi import APIRouter, Response
from starlette import status

metrics_router = APIRouter()
tag = 'Metrics'


@metrics_router.get('/metrics',
                    operation_id='metrics',
                    description='Service metrics',
                    status_code=status.HTTP_200_OK,
                    include_in_schema=False,
                    tags=[tag])
async def metrics():
    return Response(status_code=200)
