from pydantic import BaseModel
from typing import List, Optional

# Schema para Empresa (Entrada e Saída)
class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

# Schema para criar uma Empresa (sem ID)
class EmpresaCreate(EmpresaBase):
    pass

# Schema para retornar uma Empresa (com ID)
class Empresa(EmpresaBase):
    id: int

    class Config:
        orm_mode = True


# Schema para Obrigação Acessória (Entrada e Saída)
class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str  # Mensal, trimestral, anual

# Schema para criar uma Obrigação Acessória (sem ID)
class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    empresa_id: int

# Schema para retornar uma Obrigação Acessória (com ID)
class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int
    empresa_id: int

    class Config:
        orm_mode = True
