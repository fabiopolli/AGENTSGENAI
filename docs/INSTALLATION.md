# 📌 Instalação e Configuração

## 🔹 Requisitos
Antes de começar, certifique-se de ter instalado:

- **Python 3.9+**
- **Node.js 18+**
- **Docker e Docker Compose**
- **Git**

## 🔹 Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Instale as dependências do backend**
    cd backend
    pip install -r requirements.txt

3. **Instale as dependências do frontend**
    cd ../frontend
    npm install

4. **Configure as variáveis de ambiente** 
   Renomeie .env.example para .env e preencha as credenciais necessárias.

🚀 Executando o Projeto
🔹 Localmente
1. **Backend**
    cd backend
    uvicorn src.api.app:app --reload --host 0.0.0.0 --port 5000

2. **Frontend**
    cd frontend
    npm start

 


   