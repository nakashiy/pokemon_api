import sys

sys.path.append("/work")
import lib.OpenSearchRequest as OpenSearchRequest
import lib.OpenSearchApiClient as OpenSearchApiClient
import schema.PokemonModel as PokemonModel

# リクエストパラメータ設定
DeleteDocModel = PokemonModel.DeleteDocModel(
    id=1,
)
# リクエストデータ作成
DeleteDocRequest = OpenSearchRequest.DeleteDocRequest(DeleteDocModel)
# 登録リクエスト実行
OpenSearchApiClient = OpenSearchApiClient.OpenSearchApiClient()
result = OpenSearchApiClient.delete(DeleteDocRequest)
