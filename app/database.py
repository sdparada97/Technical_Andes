# imports for the MongoDB database connection
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from contextlib import asynccontextmanager

from .settings import settings

DATABASE_URL = settings.DATABASE_URL


@asynccontextmanager
async def mongo_lifespan(app: FastAPI):
    await startup_db_client(app)
    yield
    await shutdown_db_client(app)


async def startup_db_client(app):
    try:
        app.mongodb_client = AsyncIOMotorClient(DATABASE_URL)
        app.mongodb = app.mongodb_client.get_database("pokemon")
        collection_names = await app.mongodb.list_collection_names()
        if "pokemons" not in collection_names:
            await app.mongodb.create_collection("pokemons", capped=False)
        print("MongoDB connected.")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise


async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("Database disconnected.")
