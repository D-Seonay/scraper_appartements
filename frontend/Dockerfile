# Dockerfile
FROM node:14

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers package.json et package-lock.json pour installer les dépendances
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier tout le contenu du dossier frontend dans le conteneur, y compris public et src
COPY . .

# Construire l'application React
RUN npm run build

# Exposer le port que l'application utilise
EXPOSE 3000

# Commande pour démarrer l'application
CMD ["npm", "start"]
