# Usa l’immagine di Node.js
FROM node:18

# Crea una directory di lavoro
WORKDIR /app

# Copia package.json e installa le dipendenze
COPY package*.json ./
RUN npm install

# Copia tutto il resto
COPY . .

# Avvia l’app React
CMD ["npm", "start"]
