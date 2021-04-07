FROM node:12.18.1-alpine AS buid
WORKDIR /app
COPY packege.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.19.0-apline AS prod-stage
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]