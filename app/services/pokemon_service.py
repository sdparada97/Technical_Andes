from fastapi import Request
from app.repositories.pokemon_repository import PokemonRepository


class PokemonService:
    def __init__(self, repository: PokemonRepository):
        self.repository = repository

    async def get_general_info(self, request: Request, name_or_id: str):
        return await self.repository.get_general_info(request, name_or_id)

    async def get_specific_info(self, request: Request, name_or_id: str):
        return await self.repository.get_specific_info(request, name_or_id)

    async def update_pokemon_info(self, request: Request, id: str, body: dict):
        return await self.repository.update_by_name_or_id(request, id, body)
