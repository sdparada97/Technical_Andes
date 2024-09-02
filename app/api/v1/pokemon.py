from fastapi import APIRouter, Depends, HTTPException, Request

from app.repositories.pokemon_repository import PokemonRepository
from app.services.pokemon_service import PokemonService


router = APIRouter()


def get_pokemon_repository():
    return PokemonRepository()


def get_pokemon_service(repository: PokemonRepository = Depends(get_pokemon_repository)):
    return PokemonService(repository)


@router.get("/general/{name_or_id}")
async def get_general_pokemon_info(request: Request, name_or_id: str, service: PokemonService = Depends(get_pokemon_service)):
    """
    Endpoint para obtener información general del Pokémon.
    """
    try:
        return await service.get_general_info(request, name_or_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")


@router.get("/especifico/{name_or_id}")
async def get_specific_pokemon_info(request: Request, name_or_id: str, service: PokemonService = Depends(get_pokemon_service)):
    """
    Endpoint para obtener información específica del Pokémon.
    """
    try:
        return await service.get_specific_info(request, name_or_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")


@router.put("/especifico/{id}")
async def update_specific_pokemon_info(request: Request, id: str, body: dict, service: PokemonService = Depends(get_pokemon_service)):
    """
    Endpoint para actualizar información específica del Pokémon.
    """
    try:
        return await service.update_pokemon_info(request, id, body)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")
