import logging

# Configura o logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Banco de respostas pré-definidas para evitar chamadas desnecessárias à OpenAI
STATIC_ANSWERS = {
    "quantos habitantes tem são paulo?": "Segundo estimativas do IBGE em 2021, São Paulo tem aproximadamente 12,3 milhões de habitantes.",
    "qual é a capital da frança?": "A capital da França é Paris.",
    "qual é a capital do brasil": "A capital do Brasil é Brasília."
}

def fetch_search_results(user_input: str):
    # Normaliza a pergunta para evitar diferenças de maiúsculas/minúsculas
    normalized_input = user_input.lower().strip()

    # Se a resposta já está no banco, retorna sem chamar a OpenAI
    if normalized_input in STATIC_ANSWERS:
        logger.debug(f"🔍 Resposta encontrada no banco local: {STATIC_ANSWERS[normalized_input]}")
        return [STATIC_ANSWERS[normalized_input]]

    # Se não encontrar, retorna uma lista vazia, forçando o Agente Conversacional a responder
    return []