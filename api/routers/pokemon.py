from fastapi import APIRouter, Depends, FastAPI, Request
import schemas.pokemon as pokemon_schema
import crud.pokemon as pokemon_crud

router = APIRouter(prefix="/v1", tags=["pokemon"])
app = FastAPI()


@router.get("/pokemon", response_model=pokemon_schema.PokemonResponseModel)
async def detail(PokemonRequestModel: pokemon_schema.PokemonRequestModel = Depends()):
    return pokemon_crud.get_detail(PokemonRequestModel)


@router.get("/pokemons", response_model=pokemon_schema.PokemonsResponseModel)
async def list(request: Request, PokemonsRequestModel: pokemon_schema.PokemonsRequestModel = Depends()):
    return pokemon_crud.get_list(request, PokemonsRequestModel)
