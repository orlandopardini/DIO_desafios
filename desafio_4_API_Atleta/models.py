from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from database import Base

class Categoria(Base):
    __tablename__ = "categoria"
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    nome = Column(String(40), nullable=False)

class CentroTreinamento(Base):
    __tablename__ = "centro_treinamento"
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    nome = Column(String(20))
    endereco = Column(String(60))
    proprietario = Column(String(30))

class Atleta(Base):
    __tablename__ = "atleta"
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    nome = Column(String(50))
    cpf = Column(String(11), unique=True)
    idade = Column(Integer)
    peso = Column(Float(10, 2))
    altura = Column(Float(10, 2))
    sexo = Column(String(1))
    centro_treinamento_id = Column(Integer, ForeignKey("centro_treinamento.pk_id"))
    categoria_id = Column(Integer, ForeignKey("categoria.pk_id"))
