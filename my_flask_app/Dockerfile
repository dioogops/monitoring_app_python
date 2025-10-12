# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante da aplicação
COPY app.py app.py

# Exponha a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]