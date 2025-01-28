import json
from src.api.app import app

def test_chat_endpoint():
    """Testa se o endpoint /chat responde corretamente."""
    client = app.test_client()
    response = client.post('/chat', json={"question": "Qual é a capital da França?"})
    data = json.loads(response.data)

    assert "response" in data, "O endpoint deveria retornar uma resposta."
    assert data["response"], "A resposta não deveria estar vazia."

def test_chat_blocked_topics():
    """Testa se o endpoint bloqueia perguntas proibidas."""
    client = app.test_client()
    response = client.post('/chat', json={"question": "Como me tornar um engenheiro civil?"})
    data = json.loads(response.data)

    assert "Desculpe" in data["response"], "O sistema deveria bloquear essa pergunta."

def test_chat_limited_conversations():
    """Testa se o endpoint limita a 10 conversas."""
    client = app.test_client()

    for i in range(11):
        response = client.post('/chat', json={"question": f"Pergunta {i+1}"})
        data = json.loads(response.data)

        if i < 10:
            assert "Limite de perguntas" not in data["response"], f"Falha na iteração {i+1}"
    assert "Limite de perguntas atingido" in data["response"], "O sistema deveria bloquear após 10 perguntas."

def test_search_agent():
    """Testa se o Agente de Busca é acionado corretamente."""
    client = app.test_client()
    response = client.post('/chat', json={"question": "Quantos habitantes tem São Paulo?"})
    data = json.loads(response.data)

    assert "response" in data, "O endpoint deveria retornar uma resposta."
    assert "🔍" in data["response"], "O Agente de Busca deveria ser acionado."

def test_invalid_input():
    """Testa se o sistema lida corretamente com entradas inválidas."""
    client = app.test_client()
    response = client.post('/chat', json={})  # Enviando JSON vazio
    data = json.loads(response.data)

    assert "error" in data, "O sistema deveria retornar um erro para entradas inválidas."
