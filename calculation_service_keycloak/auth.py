from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

# https://anqorithm.medium.com/integrating-fastapi-with-keycloak-for-authentication-151d0996afbc
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8080/realms/master/protocol/openid-connect/token")

# Это нужно будет заранее скопировать из keycloak -> Realm Settings -> Keys -> RS256 -> Public Key
PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzPC3tU/Q3peGcjkcWcgj1+H46GGj8pdk6GBqHgsKIkHXrcBn2KcytZSN4ECB2z82kA2W7XFPZSqY0RvysexGBfoUPOBAO3kCOPwuESgSvHJUlIueZERpsbrFQ9Bc2oa33emmSlbE9IfUWg4ahMO/LTkTbfgOHxxdHGM46kOEWANHsdqstu5fiAloUPE7bLbHjsOgtNJcybaHwMsLQzGr+kyjTe76bty7FgUbPHAmN/D0GwKwT/zXevMgcOYtzA2ivUJEO8LXxTfZp5taAJqxhsjch4EJ6HmCLuDEduyiuhvrGB9bRyyv6SkT4hj1bCareANXAFl6NhYeLgV1/NEinQIDAQAB
-----END PUBLIC KEY-----
"""

ALGORITHM = "RS256"

def decode_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM], options={"verify_aud": False})
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
