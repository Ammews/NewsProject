#Importa a imagem do python
FROM python:3.14-slim

WORKDIR /app

#Copia os requerimentos pra rodar a aplicação
COPY requirements.txt .

#instala eles
RUN pip install --no-cache-dir -r requirements.txt

#copia tudo pro dockerp
COPY . .

# Roda o projeto
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
