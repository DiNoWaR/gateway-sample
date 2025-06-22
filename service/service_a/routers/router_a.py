from fastapi import APIRouter
from starlette import status

service_a_router = APIRouter()
tag = 'Service A'


@service_a_router.get('/a_health',
                      operation_id='service_a_healthCheck',
                      status_code=status.HTTP_200_OK,
                      tags=[tag])
async def health_check():
    return {
        'service': 'A',
        'status': 'ok'
    }
