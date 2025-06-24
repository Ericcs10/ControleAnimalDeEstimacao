from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.core.database import db


SECRET_KEY = "secret_key_super_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Criptografia da senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Para pegar o token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# Hash e verificação de senha
def verificar_senha(senha_plana, senha_hash):
    return pwd_context.verify(senha_plana, senha_hash)


def gerar_hash_senha(senha):
    return pwd_context.hash(senha)


# Criar JWT
def criar_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Verificar JWT
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não autorizado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        user = await db["usuarios"].find_one({"email": email})
        if user is None:
            raise credentials_exception
        user["id"] = str(user["_id"])
        user.pop("_id", None)
        return user
    except JWTError:
        raise credentials_exception
