# ⚙️ Configuração do Ambiente

O projeto utiliza um arquivo `.env` para armazenar credenciais e configurações sensíveis. 

## 🔹 Configuração de Credenciais

Para configurar corretamente:
```bash
cp backend/.env.example backend/.env
nano backend/.env


 Exemplo de Arquivo .env
OPENAI_API_KEY=your-openai-api-key
LLAMAGUARD_API_KEY
USE_LLAMAGUARD
FLASK_DEBUG
BACKEND_PORT=5000
FRONTEND_PORT=3000

🔹 Configuração no Docker
Se estiver usando Docker, as variáveis são passadas no docker-compose.yaml:
services:
  backend:
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - SERPER_API_KEY=${SERPER_API_KEY}
