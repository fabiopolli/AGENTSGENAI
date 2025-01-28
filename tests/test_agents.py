import pytest
from src.workflows.genai_flow import genai_flow

@pytest.mark.asyncio
async def test_engineering_civil_block():
    """Testa se o sistema bloqueia perguntas sobre Engenharia Civil."""
    result = await genai_flow("Fale sobre Engenharia Civil e suas vertentes")
    assert "Desculpe" in result["response"], "A resposta deveria bloquear esse assunto."

@pytest.mark.asyncio
async def test_career_advice_block():
    """Testa se o sistema bloqueia perguntas sobre carreira e emprego."""
    result = await genai_flow("Qual a melhor faculdade para engenharia?")
    assert "Desculpe" in result["response"], "A resposta deveria bloquear assuntos de carreira."

@pytest.mark.asyncio
async def test_conversational_agent_limited():
    """Testa se o Agente Conversacional limita a 10 perguntas."""
    for i in range(11):
        result = await genai_flow(f"Pergunta número {i+1}")
    
    assert "Limite de perguntas atingido" in result["response"], "O agente deveria bloquear após 10 perguntas."

@pytest.mark.asyncio
async def test_busca_acionada():
    """Testa se o Agente de Busca é acionado quando necessário."""
    result = await genai_flow("Quantos habitantes tem São Paulo?")
    assert "🔍" in result["response"], "O Agente de Busca deveria ser acionado."

@pytest.mark.asyncio
async def test_busca_max_10_results():
    """Testa se o Agente de Busca retorna no máximo 10 resultados."""
    result = await genai_flow("Preciso fazer uma busca sobre Langchain.")
    assert len(result["search_results"]) <= 10, "A busca retornou mais de 10 resultados."

@pytest.mark.asyncio
async def test_busca_nao_aciona_conversational():
    """Testa se o Agente de Busca responde diretamente sem acionar o Conversacional quando já tem a resposta."""
    result = await genai_flow("Quantos habitantes tem São Paulo?")
    assert "🔍" in result["response"], "O Agente de Busca deveria ter respondido diretamente."
