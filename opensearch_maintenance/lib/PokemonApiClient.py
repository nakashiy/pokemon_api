import requests


class PokemonApiClient:
    url1 = "https://pokeapi.co/api/v2/pokemon/"
    url2 = "https://pokeapi.co/api/v2/pokemon-species/"
    # APIで取得したデータ
    response = {}
    # 返却するポケモンのデータ
    pokemon = {}

    def __init__(self, number):
        self.response["pokemon"] = requests.get(self.url1 + str(number)).json()
        self.response["pokemon-species"] = requests.get(self.url2 + str(number)).json()

    def get(self):
        self._setNumber()
        self._setName()
        self._setTypes()
        self._setStats()
        self._setText()
        self._setImageUrl()
        return self.pokemon

    def _setNumber(self):
        self.pokemon["number"] = self.response["pokemon"]["id"]

    def _setName(self):
        self.pokemon["name"] = "なし"
        for name in self.response["pokemon-species"]["names"]:
            if name["language"]["name"] == "ja-Hrkt":
                self.pokemon["name"] = name["name"]

    def _setTypes(self):
        self.pokemon["types"] = []
        for type in self.response["pokemon"]["types"]:
            res = requests.get(type["type"]["url"]).json()
            for name in res["names"]:
                if name["language"]["name"] == "ja-Hrkt":
                    self.pokemon["types"].append(name["name"])

    def _setStats(self):
        self.pokemon["stats"] = {}
        total_stats = 0
        for stat in self.response["pokemon"]["stats"]:
            if stat["stat"]["name"] == "hp":
                self.pokemon["stats"]["hp"] = stat["base_stat"]
                total_stats += stat["base_stat"]
            if stat["stat"]["name"] == "attack":
                self.pokemon["stats"]["attack"] = stat["base_stat"]
                total_stats += stat["base_stat"]
            if stat["stat"]["name"] == "defense":
                self.pokemon["stats"]["defense"] = stat["base_stat"]
                total_stats += stat["base_stat"]
            if stat["stat"]["name"] == "special-attack":
                self.pokemon["stats"]["special_attack"] = stat["base_stat"]
                total_stats += stat["base_stat"]
            if stat["stat"]["name"] == "special-defense":
                self.pokemon["stats"]["special_defense"] = stat["base_stat"]
                total_stats += stat["base_stat"]
            if stat["stat"]["name"] == "speed":
                self.pokemon["stats"]["speed"] = stat["base_stat"]
                total_stats += stat["base_stat"]
        self.pokemon["stats"]["total"] = total_stats

    def _setText(self):
        def getVersionName(id):
            version = requests.get(f"https://pokeapi.co/api/v2/version/{id}/").json()
            for name in version["names"]:
                if name["language"]["name"] == "ja-Hrkt":
                    return name["name"]
            return ""

        self.pokemon["texts"] = []
        for flavor_text in self.response["pokemon-species"]["flavor_text_entries"]:
            text = {}
            languages = ["ja"]
            if flavor_text["language"]["name"] in languages:
                # バージョン名を日本語で取得する場合
                # tmp["version"] = getVersionName(text["version"]["url"][-3:-1])
                text["version"] = flavor_text["version"]["name"]
                text["text"] = flavor_text["flavor_text"]
            if text != {}:
                self.pokemon["texts"].append(text)

    def _setImageUrl(self):
        self.pokemon["images"] = {}
        self.pokemon["images"]["front_default"] = self.response["pokemon"]["sprites"]["front_default"]
        self.pokemon["images"]["back_default"] = self.response["pokemon"]["sprites"]["back_default"]
