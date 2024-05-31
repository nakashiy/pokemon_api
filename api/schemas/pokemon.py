from typing import Optional
from pydantic import BaseModel, Field
from fastapi import Query


class PokemonBaseModel(BaseModel):
    number: Optional[int] = Field(None, description="No")
    name: Optional[str] = Field(None, description="名前")
    types: Optional[list[str]] = Field(None, description="タイプ")
    stats: Optional[dict] = Field(None, description="ステータス")
    texts: Optional[list[dict]] = Field(None, description="説明")
    images: Optional[dict] = Field(None, description="画像")
    updated_time: Optional[str] = Field(None, description="更新日時")


class PokemonResponseModel(PokemonBaseModel):
    pass


class PokemonsResponseModel(BaseModel):
    total: int = Field(0, description="検索結果件数")
    page: int = Field(0, description="現ページ")
    next_page_uri: Optional[str] = Field(None, description="次ページ")
    data: list[PokemonBaseModel] = Field(None)


# 単体を取得するリクエスト
class PokemonRequestModel(BaseModel):
    id: int = Field(description="ID")


# 一覧を取得するリクエストのデフォルト値
class PokemonsRequestDefault:
    sort = ["number"]
    offset = 0
    size = 20


# 一覧を取得するリクエスト
class PokemonsRequestModel(BaseModel):
    number: Optional[int] = Field(Query(None, description="No"))
    number_from: Optional[int] = Field(Query(None, description="No[開始]"))
    number_to: Optional[int] = Field(Query(None, description="No[終了]"))
    name: Optional[str] = Field(Query(None, description="名前"))
    types: list[str] = Field(Query([], description="タイプ"))
    hp_from: Optional[int] = Field(Query(None, description="HP[開始]"))
    hp_to: Optional[int] = Field(Query(None, description="HP[終了]"))
    attack_from: Optional[int] = Field(Query(None, description="攻撃[開始]"))
    attack_to: Optional[int] = Field(Query(None, description="攻撃[終了]"))
    defense_from: Optional[int] = Field(Query(None, description="防御[開始]"))
    defense_to: Optional[int] = Field(Query(None, description="防御[終了]"))
    special_attack_from: Optional[int] = Field(Query(None, description="特攻[開始]"))
    special_attack_to: Optional[int] = Field(Query(None, description="特攻[終了]"))
    special_defense_from: Optional[int] = Field(Query(None, description="特防[開始]"))
    special_defense_to: Optional[int] = Field(Query(None, description="特防[終了]"))
    speed_from: Optional[int] = Field(Query(None, description="素早さ[開始]"))
    speed_to: Optional[int] = Field(Query(None, description="素早さ[終了]"))
    total_stats_from: Optional[int] = Field(Query(None, description="合計ステータス[開始]"))
    total_stats_to: Optional[int] = Field(Query(None, description="合計ステータス[終了]"))
    texts: list[str] = Field(Query([], description="説明"))
    sort: list[str] = Field(Query(PokemonsRequestDefault.sort, description="並び順[(例)昇順:number,降順:-number]"))
    offset: Optional[int] = Field(Query(PokemonsRequestDefault.offset, description="開始位置"))
    size: Optional[int] = Field(Query(PokemonsRequestDefault.size, description="取得件数"))
