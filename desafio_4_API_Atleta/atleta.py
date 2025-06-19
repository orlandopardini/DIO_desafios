from fastapi import APIRouter, HTTPException
from schemas import AtletaIn, AtletaOut, AtletaUpdate
from database import SessionLocal
from models import Atleta
import uuid

router = APIRouter(
    prefix="/atletas",
    tags=["atletas"]
)

@router.post("/", response_model=AtletaOut)
def create_atleta(atleta: AtletaIn):
    # lógica de criação usando SQLAlchemy
    pass

# GET, PATCH, DELETE...
