from pydantic import BaseModel, EmailStr, Field, field_validator


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=30,
        description='Password length must be from 8 to 30 characters long'
    )

    @field_validator('password')
    @classmethod
    def check_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError('Password must not be empty')
        return value


class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=30,
        description='Password length must be from 8 to 30 characters long'
    )

    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return value


class RefreshTokenRequest(BaseModel):
    refresh_token: str = Field(
        description='Current refresh token'
    )

    @field_validator('refresh_token')
    @classmethod
    def check_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError('Token must not be empty')
        return value


class UserAuthResponse(BaseModel):
    access_token: str
    refresh_token: str


class ErrorResponse(BaseModel):
    detail: str
