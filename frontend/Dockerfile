## Para me lembrar futuramente:

# Usa como imagem o node e dá o nome de build para usar futuramente
FROM node:22 AS build

#cria o diretorio /app, onde ficarão as informações, /app é usado por costume
WORKDIR /app

# Baixa as dependencias do projeto 
COPY package*.json ./
RUN npm install

# Copia o frontend pro docker pra poder buildar
COPY . .
RUN npm run build -- --configuration production

# Aqui é pro nginx fazer o reverse proxy com o angular, então pega a imagem do nginx
FROM nginx:alpine

#copia a imagem feita anteriormente e manda pra pasta raiz que roda no nginx
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf