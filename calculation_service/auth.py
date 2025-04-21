import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional

# Это ключ, который используется для подписания JWT в Django
DJANGO_SECRET_KEY = "django-insecure-*sow#pge_h(fmu1x(^el_vp5lk!o07pq7s$lb&_=@3v$9r0%7^"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_jwt_token(token: str):
    try:
        # Проверяем и декодируем JWT
        payload = jwt.decode(token, DJANGO_SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# Создаём зависимость для проверки авторизации
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_jwt_token(token)
    print('PAYLOAD:', payload)
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    return user_id
