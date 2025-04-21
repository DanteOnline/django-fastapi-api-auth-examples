from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

# https://anqorithm.medium.com/integrating-fastapi-with-keycloak-for-authentication-151d0996afbc
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8080/realms/master/protocol/openid-connect/token")

# Это нужно будет заранее скопировать из keycloak -> Realm Settings -> Keys -> RS256 -> Public Key
PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA42TKT9XjVLkZvebWzToaeMbPlRE7QVQFpvJA5bnsuVz2vfyajdLl6s2p52tM+i4veDP15pxGO7lzwOwXcsWtahGwMSO9bX2jNZpPoaSpKlcVKYT/CKI98346NyzwqcIlO514i8320SYKfb2GIq47FDzZXl0klEp9FpIeb9ENr1qXXvahKqX30xHDJAP5Ezx4w7LXRp2M3E/Hrg/JaYAsNcpgCKxx1w92sXqPKmyR5dBo+UxRSh/RjhpbgfEkmgLOf+svDJ2Fn7/zl5ULrxcuOaxpdR8xzBIwefFm3fBusxTlBPdDJt7EmXMNsi5ogBbt/CPidAzXnVsHTgEkANgV8QIDAQAB
-----END PUBLIC KEY-----
"""

ALGORITHM = "RS256"

def decode_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM], options={"verify_aud": False})
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
