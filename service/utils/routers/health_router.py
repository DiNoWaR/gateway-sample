from fastapi import APIRouter, Response
from starlette import status

health_router = APIRouter()
tag = 'Health Check'


@health_router.get('/health',
                   operation_id='healCheck',
                   description='Service health check',
                   status_code=status.HTTP_200_OK,
                   include_in_schema=False,
                   tags=[tag])
async def health_check():
    return Response(status_code=200)
