from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
import models, schemas

# ** Ailton Guilherme Ribeiro Ribas - https://github.com/Ribashow666 **

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# **ENDPOINTS PARA EMPRESA**

@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.cnpj == empresa.cnpj).first()
    if db_empresa:
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")
    db_empresa = models.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/", response_model=List[schemas.Empresa])
def read_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()

@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

# **ENDPOINTS PARA OBRIGAÇÃO ACESSÓRIA**

@app.post("/obrigacoes_acessorias/", response_model=schemas.ObrigacaoAcessoria)
def create_obrigacao_acessoria(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/obrigacoes_acessorias/", response_model=List[schemas.ObrigacaoAcessoria])
def read_obrigacoes_acessorias(db: Session = Depends(get_db)):
    return db.query(models.ObrigacaoAcessoria).all()

@app.get("/obrigacoes_acessorias/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def read_obrigacao_acessoria(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação Acessória não encontrada")
    return db_obrigacao
