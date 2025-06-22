from fastapi import APIRouter
from starlette import status

service_b_router = APIRouter()
tag = 'Service B'


@service_b_router.get('/b_health',
                      operation_id='service_b_healthCheck',
                      status_code=status.HTTP_200_OK,
                      tags=[tag])
async def health_check():
    return {
        'service': 'B',
        'status': 'ok'
    }
