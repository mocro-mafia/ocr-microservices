import base64
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from .models.user import User
from .config.settings import settings

def safe_b64decode(encoded_key: str) -> str:
    try:
        # Pad the base64 string if needed
        padded_key = encoded_key + '=' * ((4 - len(encoded_key) % 4) % 4)
        return base64.b64decode(padded_key).decode('utf-8')
    except Exception as e:
        print(f"Error decoding key: {e}")
        return ""

class Settings(BaseModel):
    authjwt_algorithm: str = settings.JWT_ALGORITHM
    authjwt_decode_algorithms: List[str] = [settings.JWT_ALGORITHM]
    authjwt_token_location: set = {'cookies', 'headers'}
    authjwt_access_cookie_key: str = 'access_token'
    authjwt_refresh_cookie_key: str = 'refresh_token'
    authjwt_cookie_csrf_protect: bool = False
    authjwt_public_key: str = safe_b64decode(settings.JWT_PUBLIC_KEY)
    authjwt_private_key: str = safe_b64decode(settings.JWT_PRIVATE_KEY)

@AuthJWT.load_config
def get_config():
    return Settings()

class NotVerified(Exception):
    pass

class UserNotFound(Exception):
    pass

async def require_user(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        user_id = Authorize.get_jwt_subject()
        
        user = await User.get(str(user_id))
        
        if not user:
            raise UserNotFound('User no longer exist')
        
        # Uncomment if you want to check user verification
        # if not user["verified"]:
        #     raise NotVerified('You are not verified')
        
    except Exception as e:
        error = e.__class__.__name__
        print(e)
        
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail='You are not logged in'
            )
        
        if error == 'UserNotFound':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail='User no longer exist'
            )
        
        if error == 'NotVerified':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail='Please verify your account'
            )
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Token is invalid or has expired'
        )
    
    return user_id