from pydantic import BaseModel
from typing import List

class ItemCreate(BaseModel):
    responsavel: str
    local: str
    valor: float
    datauso: str

class ItemsDelete(BaseModel):
    ids: List[int]