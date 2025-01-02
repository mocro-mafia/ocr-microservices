from fastapi import Header, HTTPException
from typing import Optional

async def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(401, "Missing authorization token")
    # Add token verification logic
    return True
