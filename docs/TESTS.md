# 🧐 Testes Automatizados

Os testes garantem que o sistema funciona corretamente, cobrindo a lógica de **bloqueio de temas proibidos, limite de perguntas e agentes de busca/conversação**.

## 🔹 Executando Testes Localmente
Para rodar os testes localmente:
```bash
pytest backend/tests --disable-warnings


🔹 Executando Testes no Docker
docker-compose run tests

🔹 Principais Testes Implementados

1. Testa bloqueio de temas proibidos
@pytest.mark.asyncio
async def test_engineering_civil_block():
    result = await genai_flow("Fale sobre Engenharia Civil")
    assert "Desculpe" in result["response"]

2. Testa limite de perguntas
    @pytest.mark.asyncio
async def test_conversational_agent_limited():
    for i in range(11):
        result = await genai_flow(f"Pergunta número {i+1}")
    assert "Limite de perguntas atingido" in result["response"]


    

