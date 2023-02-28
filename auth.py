import time
import jwt
from app import app, setting
from fastapi import HTTPException

# to response token
def token_response(token: str):
    return {
        "access token": token
    }


# to sign token
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "exp": time.time() + 600
    }
    token = jwt.encode(payload, setting.SECRET_KEY, setting.ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decodeToken = jwt.decode(token, setting.SECRET_KEY, setting.ALGORITHM)
        exp = decodeToken.get("exp")
        if exp < time.time():
            return decodeToken
    except jwt.exceptions.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")
