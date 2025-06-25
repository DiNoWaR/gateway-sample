from fastapi import APIRouter
from starlette import status
from service.auth_service.routers.model.model import UserLoginRequest, UserRegisterRequest, UserAuthResponse, \
    RefreshTokenRequest, ErrorResponse

auth_service_router = APIRouter()
tag = 'User Auth'


@auth_service_router.post('/auth/tokens',
                          operation_id='loginUser',
                          description='Login user',
                          status_code=status.HTTP_200_OK,
                          response_model=UserAuthResponse,
                          responses={
                              401: {'model': ErrorResponse, 'description': 'Invalid email or password'},
                              422: {'model': ErrorResponse, 'description': 'Bad request'},
                              500: {'model': ErrorResponse, 'description': 'Internal server error'},
                          },
                          tags=[tag])
async def login(request: UserLoginRequest):
    return UserAuthResponse(
        access_token='',
        refresh_token=''
    )


@auth_service_router.post('/auth/token/refresh',
                          operation_id='refreshToken',
                          description='Refresh access token for user',
                          status_code=status.HTTP_200_OK,
                          response_model=UserAuthResponse,
                          responses={
                              401: {'model': ErrorResponse, 'description': 'Invalid token provided'},
                              422: {'model': ErrorResponse, 'description': 'Bad request'},
                              500: {'model': ErrorResponse, 'description': 'Internal server error'},
                          },
                          tags=[tag])
async def refresh_token(request: RefreshTokenRequest):
    return UserAuthResponse(
        access_token='',
        refresh_token=''
    )


@auth_service_router.post('/users',
                          operation_id='registerUser',
                          description='Register user',
                          status_code=status.HTTP_200_OK,
                          response_model=UserAuthResponse,
                          responses={
                              422: {'model': ErrorResponse, 'description': 'Bad request'},
                              500: {'model': ErrorResponse, 'description': 'Internal server error'},
                          },
                          tags=[tag])
async def register(request: UserRegisterRequest):
    return UserAuthResponse(
        access_token='',
        refresh_token=''
    )
