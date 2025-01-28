# 📡 Referência da API

## 🔹 Endpoint Principal (`/chat`)
- **Método:** `POST`
- **URL:** `/chat`
- **Entrada:**
```json
{
  "question": "Quantos habitantes tem São Paulo?"
}

**Saída:**  
{
  "response": "Segundo o IBGE, São Paulo tem aproximadamente 12,3 milhões de habitantes."
}

🔹 Outros Endpoints
/health
Descrição: Verifica o status da API.
Método: GET
Retorno: {"status": "ok"}
/metrics
Descrição: Retorna métricas de uso da API.
Método: GET
Retorno:
{
  "total_requests": 100,
  "average_response_time": "0.8s"
}
