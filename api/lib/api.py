from opensearchpy import OpenSearch


class OpenSearchApiClient:
    # クライアントライブラリ
    client = None

    # 接続
    endpoint = "opensearch"
    port = 9200
    auth = ("admin", "admin")

    # ソート
    sorts = []

    # body
    body = None

    def __init__(self):
        self.client = OpenSearch(
            hosts=[{"host": self.endpoint, "port": self.port}],
            http_compress=True,
            http_auth=self.auth,
            use_ssl=True,
            verify_certs=False,
        )

    def get_doc(self, OpenSearchRequest):
        response = self.client.get(
            index=OpenSearchRequest.index,
            id=OpenSearchRequest.id,
            ignore=[404],
        )
        return response

    def search(self, OpenSearchRequest):
        print(OpenSearchRequest)
        response = self.client.search(
            index=OpenSearchRequest.index,
            body=OpenSearchRequest.body,
            size=OpenSearchRequest.size,
            from_=OpenSearchRequest.offset,
        )
        return response
