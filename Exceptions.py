from fastapi import HTTPException

invalid_user = HTTPException(status_code=401, detail="Invalid User")
invalid_token = HTTPException(status_code=401, detail="Invalid Token")
expired_token = HTTPException(status_code=401, detail="Expired Token")