from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_router import api_router
from app.database import mongo_lifespan
from app.middleware.auth_middleware import AuthMiddleware
from app.settings import settings

# Application starts
app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    lifespan=mongo_lifespan
)

origins = ["*"]

app.add_middleware(AuthMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)


app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Welcome Technical-Andes-Pokedex"}
