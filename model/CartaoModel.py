from pydantic import BaseModel

class ItemCreate(BaseModel):
    responsavel: str
    local: str
    valor: float
    datauso: str