import base64
from fastapi import FastAPI, HTTPException, Request, status
from starlette.middleware.base import BaseHTTPMiddleware

USERS_CREDENTIALS = {
    "andes": "andes"
}


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.users_credentials = USERS_CREDENTIALS

    async def dispatch(self, request: Request, call_next):
        if request.method != "GET":
            credentials = request.headers.get("Authorization")
            if not credentials:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="No se proporcionó ninguna credencial",
                    headers={"WWW-Authenticate": "Basic"},
                )
            try:
                decoded_bytes = base64.b64decode(credentials.split()[1])
                decoded_str = decoded_bytes.decode('ascii')
                username, password = decoded_str.split(':')
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=f"Error al decodificar las credenciales: {str(e)}",
                    headers={"WWW-Authenticate": "Basic"},
                )
            if username not in self.users_credentials or self.users_credentials[username] != password:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Credenciales inválidas",
                    headers={"WWW-Authenticate": "Basic"},
                )
            return await call_next(request)
        return await call_next(request)
