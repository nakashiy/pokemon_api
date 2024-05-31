from typing import Optional
from pydantic import BaseModel, Field


# 登録リクエストモデル
class PostDocModel(BaseModel):
    number: Optional[int] = Field(None)
    name: Optional[str] = Field(None, description="名前")
    types: Optional[list[str]] = Field(None, description="タイプ")
    stats: Optional[dict] = Field(None, description="ステータス")
    texts: Optional[list[dict]] = Field(None, description="説明")
    images: Optional[dict] = Field(None, description="画像")
    updated_time: Optional[str] = Field(None, description="更新日時")
    deleted_flg: Optional[bool] = Field(None, description="削除フラグ")


# 削除リクエストモデル
class DeleteDocModel(BaseModel):
    id: Optional[int]
