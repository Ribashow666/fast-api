from fastapi.testclient import TestClient
from main import app
from database import SessionLocal, engine
import models

# Criar as tabelas no banco de dados para os testes
models.Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_empresa():
    response = client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12345678000195",
        "endereco": "Rua Teste, 123",
        "email": "contato@empresa.com",
        "telefone": "1234567890"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"

# Teste de leitura de empresas
def test_read_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verifica se há empresas cadastradas

# Teste de leitura de uma empresa específica
def test_read_empresa():
    # Cria uma empresa para garantir que existe uma
    empresa = {
        "nome": "Empresa Teste 2",
        "cnpj": "98765432000195",
        "endereco": "Rua Teste 2, 123",
        "email": "contato2@empresa.com",
        "telefone": "9876543210"
    }
    response = client.post("/empresas/", json=empresa)
    empresa_id = response.json()["id"]

    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    assert response.json()["id"] == empresa_id

# Teste de criação de obrigação acessória
def test_create_obrigacao_acessoria():
    response = client.post("/obrigacoes_acessorias/", json={
        "nome": "Declaração de Impostos",
        "periodicidade": "Mensal",
        "empresa_id": 1
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Declaração de Impostos"

# Teste de leitura de obrigações acessórias
def test_read_obrigacoes_acessorias():
    response = client.get("/obrigacoes_acessorias/")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verifica se há obrigações cadastradas
