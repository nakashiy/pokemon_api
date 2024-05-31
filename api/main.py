from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from routers import pokemon

app = FastAPI()
app.include_router(pokemon.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="POKEMON API",
        version="1.0.0",
        summary="説明",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
