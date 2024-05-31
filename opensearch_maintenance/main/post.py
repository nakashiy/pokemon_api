import sys
from datetime import datetime

sys.path.append("/work")
import lib.PokemonApiClient as PokemonApi
import lib.OpenSearchRequest as OpenSearchRequest
import lib.OpenSearchApiClient as OpenSearchApi
import schema.PokemonModel as PokemonModel


def post(number):
    PokemonApiClient = PokemonApi.PokemonApiClient(number)
    pokemon = PokemonApiClient.get()
    now = datetime.now()
    # リクエストパラメータ設定
    PostDocModel = PokemonModel.PostDocModel(
        number=pokemon["number"],
        name=pokemon["name"],
        types=pokemon["types"],
        stats=pokemon["stats"],
        texts=pokemon["texts"],
        images=pokemon["images"],
        updated_time=now.strftime("%Y-%m-%dT%H:%M:%S"),
        deleted_flg=False,
    )
    # リクエストデータ作成
    PostDocRequest = OpenSearchRequest.PostDocRequest(PostDocModel)
    # 登録リクエスト実行
    OpenSearchApiClient = OpenSearchApi.OpenSearchApiClient()
    return OpenSearchApiClient.post(PostDocRequest)


# post(1)

start = 10
end = 25
for i in range(start, end + 1):
    result = post(i)
    print(result)
