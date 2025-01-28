# 🔄 Fluxo de Processamento com LangGraph

Este projeto utiliza **LangGraph** para estruturar e gerenciar o fluxo de conversação. O fluxo é definido em `genai_workflow.py` e segue os seguintes passos:

## 📌 Estrutura do Fluxo
1. **`detect_language`** → Detecta o idioma da entrada do usuário.
2. **`is_prohibited_topic`** → Verifica se a pergunta contém palavras proibidas e bloqueia imediatamente.
3. **`translate`** → Traduz o input para português, se necessário.
4. **`route_to_agent`** → Decide se a pergunta será processada pelo agente de busca ou pelo agente conversacional.
5. **`translate_back`** → Traduz a resposta de volta para o idioma original, se necessário.
6. **`end`** → Finaliza o fluxo e retorna a resposta ao usuário.

## 🔹 Exemplo de Fluxo no Código

```python
builder.add_node("detect_language", detect_language)  
builder.add_node("is_prohibited_topic", is_prohibited_topic)  
builder.add_node("translate", translate)  
builder.add_node("route_to_agent", route_to_agent)  
builder.add_node("translate_back", translate_back)  
builder.add_node("end", lambda state: state)

builder.add_edge(START, "detect_language")  
builder.add_edge("detect_language", "is_prohibited_topic")  
builder.add_edge("is_prohibited_topic", "translate")  
builder.add_edge("translate", "route_to_agent")  
builder.add_edge("route_to_agent", "translate_back")  
builder.add_edge("translate_back", "end")  
