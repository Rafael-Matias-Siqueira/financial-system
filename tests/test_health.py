from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    resposta = client.get("/api/health")
    assert resposta.status_code == 200

    
    resultado = resposta.json()
    

    assert resultado == {"status": "ok",
                         "application": "Meu Controle Financeiro"}

    