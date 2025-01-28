from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from langchain_community.tools import Tool

llm = ChatOpenAI(model="gpt-3.5-turbo")

# 🚫 Bloqueio avançado de palavras proibidas
PROHIBITED_KEYWORDS = ["engenharia civil", "carreira", "emprego", "trabalho", "vaga", "dicas profissionais"]

def response_filter(input_text):
    if any(keyword in input_text.lower() for keyword in PROHIBITED_KEYWORDS):
        return "Desculpe, não posso fornecer essa informação. Posso te ajudar com outras dúvidas?"

    response = llm.invoke(input_text)
    
    return response.content if hasattr(response, 'content') else str(response)

# Definição de ferramenta de exemplo
def example_tool(input_text):
    return f"A ferramenta recebeu o seguinte texto: {input_text}"

tools = [
    Tool(
        name="ExampleTool",
        func=example_tool,
        description="Uma ferramenta de exemplo que apenas retorna um texto formatado."
    )
]

# Inicializar o agente
conversational_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    handle_parsing_errors=True
)
