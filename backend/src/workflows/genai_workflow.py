from langgraph.graph import StateGraph, START
from typing_extensions import TypedDict
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Estado geral compartilhado entre os nós
class OverallState(TypedDict):
    user_input: str
    moderated_input: str
    language: str
    translated_input: str
    response: str
    conversation_count: int

# Palavras-chave proibidas
PROHIBITED_KEYWORDS = ["engenharia civil", "carreira", "emprego", "trabalho", "vaga", "dicas profissionais"]

# 🏁 Detector de idioma
def detect_language(state: OverallState) -> OverallState:
    logger.debug("Detectando idioma...")
    user_input = state["user_input"].lower()

    if "hola" in user_input:
        detected_language = "es"
    elif "bonjour" in user_input:
        detected_language = "fr"
    else:
        detected_language = "pt"
    
    logger.debug(f"Idioma detectado: {detected_language}")
    return {**state, "language": detected_language}

# 🏁 Traduzir para português (evita traduções desnecessárias)
def translate(state: OverallState) -> OverallState:
    if state["language"] != "pt" and not state["translated_input"]:
        logger.debug("Traduzindo input para o português...")
        translated_input = f"Traduzido para PT: {state['user_input']}"
        logger.debug(f"Texto traduzido: {translated_input}")
        return {**state, "translated_input": translated_input}
    
    logger.debug("Nenhuma tradução necessária.")
    return state

# 🛑 Verifica se o input contém palavras proibidas e bloqueia imediatamente
def is_prohibited_topic(state: OverallState) -> OverallState:
    if any(keyword in state["user_input"].lower() for keyword in PROHIBITED_KEYWORDS):
        logger.debug(f"🚨 Pergunta bloqueada: {state['user_input']}")
        return {
            **state,
            "response": "🚫 Desculpe, não posso responder perguntas sobre esse tema.",
            "conversation_count": state["conversation_count"]  # Não aumenta o contador
        }
    return state

# 📢 Agente conversacional (importado do `conversational_agent.py`)
from src.agents.conversational_agent import response_filter

def conversational_agent(state: OverallState) -> OverallState:
    if state["conversation_count"] >= 10:
        logger.debug("Limite de perguntas atingido.")
        return {**state, "response": "Você atingiu o limite de perguntas para essa sessão."}
    
    response = response_filter(state["translated_input"] or state["user_input"])
    logger.debug(f"Resposta gerada pelo Agente Conversacional: {response}")
    return {**state, "response": response, "conversation_count": state["conversation_count"] + 1}

# 🔎 Agente de busca (importado do `search_agent.py`)
from src.agents.search_agent import fetch_search_results

def search_agent(state: OverallState) -> OverallState:
    logger.debug("Executando busca...")
    search_results = fetch_search_results(state["user_input"])
    
    if search_results:
        response = f"Resultados da busca: {', '.join(search_results)}"
        logger.debug(f"🔍 {response}")
        return {**state, "response": response}
    
    return state  # Se não encontrou resultados, continua no fluxo normal

# 🚦 Roteamento para o agente adequado
def route_to_agent(state: OverallState) -> OverallState:
    logger.debug(f"Verificando se a pergunta pode ser respondida pelo Agente de Busca: {state['user_input']}")
    
    search_results = fetch_search_results(state["user_input"])
    
    if search_results:
        logger.debug(f"🔍 Pergunta será respondida pelo Agente de Busca: {state['user_input']}")
        return {**state, "response": search_results[0]}  # Retorna o primeiro resultado da busca
    
    logger.debug(f"💬 Pergunta será respondida pelo Agente Conversacional: {state['user_input']}")
    return conversational_agent(state)

# 🌍 Traduz resposta de volta para o idioma original (evita traduções desnecessárias)
def translate_back(state: OverallState) -> OverallState:
    if state["language"] != "pt":
        logger.debug("Traduzindo resposta de volta para o idioma original...")
        translated_response = f"Traduzido de volta para {state['language']}: {state['response']}"
        logger.debug(f"Resposta traduzida de volta: {translated_response}")
        return {**state, "response": translated_response}
    
    return state

# 🛠 Configuração do fluxo
builder = StateGraph(OverallState)

# 📌 Adiciona os nós ao fluxo
builder.add_node("detect_language", detect_language)  
builder.add_node("is_prohibited_topic", is_prohibited_topic)  
builder.add_node("translate", translate)  
builder.add_node("route_to_agent", route_to_agent)  
builder.add_node("translate_back", translate_back)  
builder.add_node("end", lambda state: state)  

# 🔄 Define as transições do fluxo
builder.add_edge(START, "detect_language")  
builder.add_edge("detect_language", "is_prohibited_topic")  # 🚨 Primeiro verifica se é proibido
builder.add_edge("is_prohibited_topic", "translate")  
builder.add_edge("translate", "route_to_agent")  
builder.add_edge("route_to_agent", "translate_back")  
builder.add_edge("translate_back", "end")  

# 🚀 Compila o fluxo
graph = builder.compile()

# 🎯 Função principal do fluxo
def genai_flow(user_input: str) -> dict:
    logger.debug(f"Iniciando fluxo com input: {user_input}")
    initial_state: OverallState = {
        "user_input": user_input,
        "moderated_input": "",
        "language": "",
        "translated_input": "",
        "response": "",
        "conversation_count": 0,
    }
    try:
        result = graph.invoke(initial_state)  # Rodando de forma síncrona
        logger.debug(f"Resultado bruto do fluxo: {result}")

        # ✅ **Correção: Pegando apenas a string da resposta**
        return {
            "response": result.get("response", ""),  # Apenas a string
        }

    except Exception as e:
        logger.error(f"Erro no fluxo: {e}")
        return {"response": "Erro ao processar o fluxo."}

