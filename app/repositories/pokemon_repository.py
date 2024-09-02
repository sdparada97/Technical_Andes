from fastapi import Request, HTTPException
from httpx import AsyncClient, HTTPStatusError
from pymongo import ReturnDocument
from bson import ObjectId

from app.repositories.base_repository import BaseRepository


class PokemonRepository(BaseRepository):
    """
    Clase encargada de manejar operaciones relacionadas con Pokémon.
    
    Esta clase hereda de BaseRepository y utiliza FastAPI y MongoDB para interactuar
    con la base de datos y la API de Pokémon.
    """
    BASE_API_URL = "https://pokeapi.co/api/v2/pokemon/"

    def __init__(self):
        super().__init__()

    async def get_by_id_or_name(self, name_or_id):
        """
        Obtiene información sobre un Pokémon por su ID o nombre.
        
        Args:
            name_or_id (str): El ID o nombre del Pokémon a buscar.
        
        Returns:
            dict: Información del Pokémon obtenido de la API.
        
        Raises:
            HTTPStatusError: Si la solicitud a la API falla.
            HTTPException: Si ocurre un error HTTP durante la operación.
        """
        try:
            async with AsyncClient() as client:
                response = await client.get(f"{self.BASE_API_URL}{name_or_id}")
                if response.status_code == 200:
                    data = response.json()
                    return data
                else:
                    raise HTTPStatusError(f"Error HTTP: {response.status_code}, Mensaje: {await response.text()}")
        except HTTPStatusError as http_err:
            raise HTTPException(status_code=response.status_code, detail=f"Error HTTP al obtener el Pokémon: {http_err}")

    async def get_general_info(self, request: Request, name_or_id: str):
        """
        Obtiene información general sobre un Pokémon.
        
        Args:
            request (Request): Objeto FastAPI para acceder al contexto del servidor.
            name_or_id (str): El ID o nombre del Pokémon a buscar.
        
        Returns:
            dict: Información básica del Pokémon incluyendo su nombre y datos obtenidos.
        
        Raises:
            HTTPException: Si ocurre un error durante la operación.
        """
        try:
            db = request.app.mongodb.get_collection('pokemons')
            processed_query = self.process_query(name_or_id)
            db_data = await db.find_one(processed_query)
            data = await self.get_by_id_or_name(name_or_id)
            if db_data:
                return {
                    "nombre": db_data["name"],
                    "recurso_de_datos": db_data
                }
            return {
                "nombre": data["name"],
                "recurso_de_datos": data
            }
        except KeyError as e:
            raise HTTPException(status_code=500, detail=f"Error al procesar la información del Pokémon: campo faltante {e}")

    async def get_specific_info(self, request: Request, name_or_id: str):
        """
        Obtiene información detallada sobre un Pokémon.
        
        Args:
            request (Request): Objeto FastAPI para acceder al contexto del servidor.
            name_or_id (str): El ID o nombre del Pokémon a buscar.
        
        Returns:
            dict: Información detallada del Pokémon incluyendo habilidades, ID, sprites y tipos.
        
        Raises:
            HTTPException: Si ocurre un error durante la operación.
        """
        try:
            db = request.app.mongodb.get_collection('pokemons')
            processed_query = self.process_query(name_or_id)
            db_data = await db.find_one(processed_query)
            data = await self.get_by_id_or_name(name_or_id)
            if db_data:
                return {
                    "name": db_data["name"],
                    "abilities": db_data["abilities"],
                    "id": db_data["id"],
                    "sprites": db_data["sprites"],
                    "types": db_data['types']
                }
            return {
                "name": data["name"],
                "abilities": data["abilities"],
                "id": data["id"],
                "sprites": data["sprites"],
                "types": data['types']
            }
        except KeyError as e:
            raise HTTPException(status_code=500, detail=f"Error al procesar la información del Pokémon: campo faltante {e}")

    async def update_by_name_or_id(self, request: Request, id, pokemon_updated_data):
        """
        Actualiza información de un Pokémon en la base de datos local.
        
        Args:
            request (Request): Objeto FastAPI para acceder al contexto del servidor.
            id (str): El ID del Pokémon a actualizar.
            pokemon_updated_data (dict): Datos actualizados del Pokémon.
        
        Returns:
            dict: Documento actualizado en la base de datos.
        
        Raises:
            HTTPException: Si ocurre un error durante la operación.
        """
        try:
            db = request.app.mongodb.get_collection('pokemons')
            pokemon_data = await self.get_by_id_or_name(id)
            updated_data_pokemon = {}
            for key, value in pokemon_updated_data.items():
                if key in pokemon_data:
                    updated_data_pokemon[key] = value
                else:
                    updated_data_pokemon[key] = value
            updated_pokemon = {**pokemon_data, **updated_data_pokemon}
            find_pokemon = await db.find_one({"id": int(id)})
            result = await db.find_one_and_update(
                {"_id": find_pokemon["_id"] if find_pokemon else str(ObjectId())}, # Filtro para encontrar el Pokémon
                {"$set": updated_pokemon},   # Datos a actualizar
                upsert=True,              # Crear si no existe
                return_document=ReturnDocument.AFTER  # Devolver el documento actualizado después de la operación
            )
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar la información del Pokémon: {e}")

    async def create(self, request):
        # Se deberan de implmentar despues
        pass

    async def get_by_id(self, id):
        # Se deberan de implmentar despues
        pass

    async def get_all(self):
        # Se deberan de implmentar despues
        pass

    async def delete_all(self):
        # Se deberan de implmentar despues
        pass

    def process_query(self, query):
        """
        Procesa la consulta para buscar un Pokémon por ID o nombre.
        
        Args:
            query (str): El ID o nombre del Pokémon a buscar.
        
        Returns:
            dict: Diccionario de consulta procesado para MongoDB.
        
        Raises:
            ValueError: Si el parámetro query no es válido.
        """
        try:
            return {"id": int(query)}
        except:  # noqa: E722
            return {"name": query.lower()}
