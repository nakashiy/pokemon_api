from lib import req as req
from lib import api as opensearch_api
import schemas.pokemon as pokemon_schema
import urllib.parse


def get_detail(PokemonRequestModel):
    # IDの指定なし
    if PokemonRequestModel.id is None:
        return pokemon_schema.PokemonResponseModel()
    # 検索リクエスト作成・検索実行
    GetDocRequest = req.GetDocRequest(PokemonRequestModel)
    OpenSearchApiClient = opensearch_api.OpenSearchApiClient()
    result = OpenSearchApiClient.get_doc(GetDocRequest)
    if result["found"] is False:
        return pokemon_schema.PokemonResponseModel()
    return result["_source"]


def _get_next_page_uri(request, total, page):
    urlparse = urllib.parse.urlparse(request.url._url)
    query = urllib.parse.parse_qs(urlparse.query)
    if query.keys() >= {"offset", "size"}:
        query["offset"][0] = int(query["size"][0]) * page
    else:
        query["offset"] = [pokemon_schema.PokemonsRequestDefault.size]
        query["size"] = [pokemon_schema.PokemonsRequestDefault.size]
    next_page_uri = urllib.parse.urlunparse(urlparse._replace(query=urllib.parse.urlencode(query, doseq=True)))
    # 最終ページでは次ページURLなし
    if total <= int(query["size"][0]) * page:
        next_page_uri = None
    return next_page_uri


def get_list(request, PokemonsRequestModel):
    # 検索リクエスト作成
    SearchRequest = req.SearchRequest(PokemonsRequestModel)
    SearchRequest.create_body()
    # 検索実行
    OpenSearchApiClient = opensearch_api.OpenSearchApiClient()
    result = OpenSearchApiClient.search(SearchRequest)
    pokemons = []
    for data in result["hits"]["hits"]:
        pokemon = data["_source"]
        pokemons.append(pokemon)
    total = result["hits"]["total"]["value"]
    page = SearchRequest.offset // SearchRequest.size + 1
    next_page_uri = _get_next_page_uri(request, total, page)
    # レスポンス作成
    PokemonsResponseModel = pokemon_schema.PokemonsResponseModel(
        page=page,
        total=total,
        next_page_uri=next_page_uri,
        data=pokemons,
    )
    return PokemonsResponseModel
