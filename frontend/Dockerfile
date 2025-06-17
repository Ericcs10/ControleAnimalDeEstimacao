# Etapa 1 - Build
FROM node:20 as build

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

# Etapa 2 - Servir o build
FROM node:20

WORKDIR /app

COPY --from=build /app /app

RUN npm install -g serve

EXPOSE 5173

CMD ["serve", "-s", "dist", "-l", "5173"]
