# Build Stage
FROM node:20-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
COPY . .

RUN npm install 
RUN npm run build

# Production Stage
FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html

# Remove default nginx config e adiciona a nossa
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
