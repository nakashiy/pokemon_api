class OpenSearchRequest:
    pass


class PokemonRequest(OpenSearchRequest):
    index = "pokemon"


class GetDocRequest(PokemonRequest):
    def __init__(self, PokemonRequestModel):
        self.id = PokemonRequestModel.id


class SearchRequest(PokemonRequest):
    def __init__(self, PokemonsRequestModel):
        self.number = PokemonsRequestModel.number
        self.number_from = PokemonsRequestModel.number_from
        self.number_to = PokemonsRequestModel.number_to
        self.name = PokemonsRequestModel.name
        self.types = PokemonsRequestModel.types
        self.hp_from = PokemonsRequestModel.hp_from
        self.hp_to = PokemonsRequestModel.hp_to
        self.attack_from = PokemonsRequestModel.attack_from
        self.attack_to = PokemonsRequestModel.attack_to
        self.defense_from = PokemonsRequestModel.defense_from
        self.defense_to = PokemonsRequestModel.defense_to
        self.special_attack_from = PokemonsRequestModel.special_attack_from
        self.special_attack_to = PokemonsRequestModel.special_attack_to
        self.special_defense_from = PokemonsRequestModel.special_defense_from
        self.special_defense_to = PokemonsRequestModel.special_defense_to
        self.speed_from = PokemonsRequestModel.speed_from
        self.speed_to = PokemonsRequestModel.speed_to
        self.total_stats_from = PokemonsRequestModel.total_stats_from
        self.total_stats_to = PokemonsRequestModel.total_stats_to
        self.texts = PokemonsRequestModel.texts
        self.sort = PokemonsRequestModel.sort
        self.offset = PokemonsRequestModel.offset
        self.size = PokemonsRequestModel.size

    # 条件追加
    def _add_condition(self, query, field, value):
        if value:
            self.body["query"]["bool"]["must"].append({query: {field: value}})

    # 範囲指定
    def _add_range_condition(self, field, operator, value):
        if value:
            self.body["query"]["bool"]["must"].append({"range": {field: {operator: value}}})

    def _add_texts_condition(self, values):
        if values:
            texts_condition = {
                "nested": {
                    "path": "texts",
                    "query": {"bool": {"must": []}},
                }
            }
            for value in values:
                texts_condition["nested"]["query"]["bool"]["must"].append({"match_phrase": {"texts.text": value}})
            self.body["query"]["bool"]["must"].append(texts_condition)

    # 条件追加(並び順)
    def _add_sort_condition(self, values):
        sortable_fields = ["number", "stats.hp", "stats.attack", "stats.defense", "stats.special_attack", "stats.special_defense", "stats.speed", "stats.total"]
        sorts = []
        for value in values:
            # 先頭文字で昇順・降順を判定
            if value[0] == "-":
                if value[1:] in sortable_fields:
                    sorts.append({value[1:]: "desc"})
            else:
                if value in sortable_fields:
                    sorts.append({value: "asc"})
        self.body["sort"] = sorts

    # リクエストボディ作成
    def create_body(self):
        self.body = {
            "query": {"bool": {"must": []}},
            "sort": [],
            "from": self.offset,
            "size": self.size,
        }

        # 必須条件
        self._add_condition("term", "deleted_flg", "false")
        # 項目ごとに条件を作成
        self._add_condition("term", "number", self.number)
        self._add_range_condition("number", "gte", self.number_from)
        self._add_range_condition("number", "lte", self.number_to)
        self._add_condition("match_phrase", "name", self.name)
        self._add_condition("terms", "types.keyword", self.types)
        self._add_range_condition("stats.hp", "gte", self.hp_from)
        self._add_range_condition("stats.hp", "lte", self.hp_to)
        self._add_range_condition("stats.attack", "gte", self.attack_from)
        self._add_range_condition("stats.attack", "lte", self.attack_to)
        self._add_range_condition("stats.defense", "gte", self.defense_from)
        self._add_range_condition("stats.defense", "lte", self.defense_to)
        self._add_range_condition("stats.special_attack", "gte", self.special_attack_from)
        self._add_range_condition("stats.special_attack", "lte", self.special_attack_to)
        self._add_range_condition("stats.special_defense", "gte", self.special_defense_from)
        self._add_range_condition("stats.special_defense", "lte", self.special_defense_to)
        self._add_range_condition("stats.speed", "gte", self.speed_from)
        self._add_range_condition("stats.speed", "lte", self.speed_to)
        self._add_range_condition("stats.total", "gte", self.total_stats_from)
        self._add_range_condition("stats.total", "lte", self.total_stats_to)
        self._add_texts_condition(self.texts)
        self._add_sort_condition(self.sort)
