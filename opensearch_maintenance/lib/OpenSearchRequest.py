# 基本リクエスト
class PokemonRequest:
    # インデックス
    index = "pokemon"


# 登録リクエスト
class PostDocRequest(PokemonRequest):
    id = ""
    body = {}

    def __init__(self, PostDocModel):
        self.id = PostDocModel.number
        self.body["number"] = PostDocModel.number
        self.body["name"] = PostDocModel.name
        self.body["types"] = PostDocModel.types
        self.body["stats"] = PostDocModel.stats
        self.body["texts"] = PostDocModel.texts
        self.body["images"] = PostDocModel.images
        self.body["updated_time"] = PostDocModel.updated_time
        self.body["deleted_flg"] = PostDocModel.deleted_flg


# 削除リクエスト
class DeleteDocRequest(PokemonRequest):
    id = ""

    def __init__(self, DeleteDocModel):
        self.id = DeleteDocModel.id
