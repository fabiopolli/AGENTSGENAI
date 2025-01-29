https://github.com/user-attachments/assets/8e8af5e9-6fd2-41e0-841f-a246ad06a9c9


AGENTS GENAI
Este repositório contém um assistente conversacional construído com LangGraph, FastAPI, React.js e Docker.

## 📦 Configuração e Instalação
Para configuração e instalação detalhada, veja o INSTALLATION.md.

## 🚀 APIs e Endpoints
Para documentação detalhada das APIs, acesse o API_REFERENCE.md.

## 💤 Fluxo do Sistema com LangGraph
Para entender o fluxo do sistema, leia o LANGGRAPH_FLOW.md.

## 🛠 Testes Automatizados
Informações detalhadas sobre testes podem ser encontradas no TESTS.md.

## 🔐 Configuração de Credenciais
Detalhes sobre como configurar variáveis de ambiente estão no CONFIGURATION.md.

##🤝 Contribuição
Se deseja contribuir para este projeto, siga os passos abaixo:

##Faça um fork do projeto e crie uma branch com suas alterações.
##Realize suas modificações e faça commits com mensagens claras.
##Crie um Pull Request detalhando suas mudanças.
##🐝 Licença
##Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.

##Arquitetura AWS
+------------------------------------+
| Amazon S3 (Front-End React Build) |
|     + AWS CloudFront (CDN)        |
+------------------------------------+
             |
             ↓
    +--------------------------+
    | AWS API Gateway          |  <--->  AWS WAF (Firewall Proteção)
    | (Gerencia requisições)   |
    +--------------------------+
             |
             ↓
+-------------------------+         +------------------------------+
|  AWS ALB (Load Balancer) | -----> | Amazon EKS - Query Service  |
|  (Distribui chamadas)    |        | (Consulta e roteamento)     |
+-------------------------+         +-------------+--------------+
                                             |                         |
                                             ↓                         ↓
                             +------------------------+    +-------------------------+
                             | Amazon EKS - Search    |    | Amazon EKS - AI Agents  |
                             | Agent (Consulta no DB) |    | Conversational Agents   |
                             +------------------------+    +-------------------------+
                                         |                           |
                                         ↓                           |
                                +----------------+                   |
                                | Amazon RDS/Aurora (DB) | <-- AWS X-Ray (Monitoramento)
                                +----------------+   


