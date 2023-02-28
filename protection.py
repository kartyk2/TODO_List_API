from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app import setting
from jwt import exceptions
import jwt

bearer = HTTPBearer()


async def authenticate(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    try:
        payload = jwt.decode(credentials.credentials, setting.SECRET_KEY, setting.ALGORITHM)
        return payload["userID"]
    except exceptions.InvalidTokenError:
        raise exceptions.InvalidTokenError

