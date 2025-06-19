from pydantic import BaseModel
from typing import Optional
import uuid

class AtletaIn(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int

class AtletaOut(AtletaIn):
    id: uuid.UUID

class AtletaUpdate(BaseModel):
    nome: Optional[str]
    idade: Optional[int]
    peso: Optional[float]
    altura: Optional[float]
