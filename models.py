from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Modelo da Empresa
class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    endereco = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    # Relacionamento com as obrigações acessórias
    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")

# Modelo de Obrigação Acessória
class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    periodicidade = Column(String, nullable=False)  # Mensal, trimestral, anual
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

    # Relacionamento com a empresa
    empresa = relationship("Empresa", back_populates="obrigacoes")
