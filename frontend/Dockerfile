# Usa uma imagem leve do Node.js
FROM node:18-alpine

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos package.json e package-lock.json para instalar dependências
COPY package.json package-lock.json ./

# Instala as dependências corretamente
RUN npm install --legacy-peer-deps

# Copia todo o código do frontend
COPY . .

# Expor a porta 3000
EXPOSE 3000

# Comando para iniciar a aplicação React
CMD ["npm", "start"]
