from opensearchpy import OpenSearch


class OpenSearchApiClient:
    client = None
    endpoint = "opensearch"
    port = 9200
    auth = ("admin", "admin")

    def __init__(self):
        self.client = OpenSearch(
            hosts=[{"host": self.endpoint, "port": self.port}],
            http_compress=True,
            http_auth=self.auth,
            use_ssl=True,
            verify_certs=False,
        )

    # 登録
    def post(self, PostDocRequest):
        response = self.client.index(
            index=PostDocRequest.index,
            id=PostDocRequest.id,
            body=PostDocRequest.body,
        )
        return response

    # 削除
    def delete(self, DeleteDocRequest):
        response = self.client.delete(
            index=DeleteDocRequest.index,
            id=DeleteDocRequest.id,
        )
        return response
