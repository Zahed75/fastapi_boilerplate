import os

from fastapi import APIRouter


def get_security_key():
    return os.getenv("SECURITY_KEY")


def get_api_key():
    return os.getenv("API_KEY")


def is_production():
    pass


def get_allowed_hosts():
    return os.getenv("ALLOWED_HOSTS")


def get_cors_allowed_origins():
    return os.getenv("CORS_ALLOW_ORIGINS")


def database_url():
    return os.getenv("DATABASE_URL")


def get_redis_url():
    return os.getenv("REDIS_URL")



def get_jwt_expiration():
    return os.getenv("JWT_EXPIRATION")



def get_max_upload_size():
    return os.getenv("MAX_UPLOAD_SIZE")


def redis_url():
    return os.getenv("REDIS_URL")