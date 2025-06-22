from fastapi import APIRouter
from starlette import status

service_c_router = APIRouter()
tag = 'Service C'


@service_c_router.get('/c_health',
                      operation_id='service_c_healthCheck',
                      status_code=status.HTTP_200_OK,
                      tags=[tag])
async def health_check():
    return {
        'service': 'C',
        'status': 'ok'
    }
