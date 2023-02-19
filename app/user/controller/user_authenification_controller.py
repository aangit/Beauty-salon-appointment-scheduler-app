
from typing import List

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.user.service.user_authentification_service import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, user_type_id: List[str], auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.user_type_id = user_type_id

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload.get("valid"):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            if payload.get("user_type_id") not in self.user_type_id:
                raise HTTPException(
                    status_code=403,
                    detail="User with provided type is not permitted to access this " "route.",
                )
            return payload
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> dict:
        is_token_valid: bool = False
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return {"valid": is_token_valid, "user_type_id": payload["user_type_id"], "user_id": payload["user_id"]}



