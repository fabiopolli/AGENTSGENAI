# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências corretamente
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos para o container
COPY . .

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar o backend
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "src.api.app:app"]
