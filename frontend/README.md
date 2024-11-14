
# Projet de Scraping d'Appartements
[![wakatime](https://wakatime.com/badge/user/018e9f6e-3f6e-41ca-8923-c1d7110b6f50/project/4a88b23a-d84f-4726-a443-8de36e8aa420.svg)](https://wakatime.com/badge/user/018e9f6e-3f6e-41ca-8923-c1d7110b6f50/project/4a88b23a-d84f-4726-a443-8de36e8aa420)

## Description

Ce projet permet de scraper des annonces d'appartements à partir d'un site web spécifique, de collecter les informations pertinentes sur chaque annonce (titre, prix, localisation, lien, image, date de scraping), et de les sauvegarder dans une base de données MongoDB pour un usage ultérieur.

Les données extraites sont accessibles via une API Flask et affichées sur un frontend React.

## Fonctionnalités

- **Scraping des annonces immobilières** : Extrait les informations des annonces immobilières (titre, prix, localisation, image, etc.).
- **Sauvegarde dans MongoDB** : Enregistre les données extraites dans une base de données MongoDB pour une utilisation ultérieure.
- **API Flask** : Permet d'accéder aux données de l'application via une API simple.
- **Frontend React** : Affiche les données de l'API dans une interface utilisateur interactive.
- **Date et heure de scraping** : Chaque annonce récupérée contient la date et l'heure de l'extraction.

## Prérequis

Avant de démarrer le projet, assurez-vous d'avoir installé les outils suivants sur votre machine :

- **Node.js** et **npm** pour gérer le frontend React.
- **Python 3.x** pour l'API Flask.
- **MongoDB** (ou utiliser MongoDB Atlas pour une version cloud).
- **Docker** (optionnel, mais recommandé pour la conteneurisation du projet).

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/D-Seonay/scraper_appartements.git
cd scraper_appartements
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Linux/macOS
venv\Scripts\activate     # Sur Windows
```

### 3. Installer les dépendances

Pour le backend Flask :

```bash
pip install -r requirements.txt
```

Pour le frontend React (dans un autre terminal, à la racine du projet) :

```bash
cd frontend
npm install
```

Les dépendances principales pour le backend sont :

- `requests` : Pour effectuer des requêtes HTTP vers le site à scraper.
- `beautifulsoup4` : Pour analyser et extraire des données à partir du HTML.
- `pymongo` : Pour interagir avec la base de données MongoDB.
- `flask` : Pour l'API.
- `flask_cors` : Pour gérer les requêtes entre différentes origines (CORS).

Les dépendances principales pour le frontend React sont :

- `axios` : Pour envoyer des requêtes HTTP à l'API Flask.
- `react-router-dom` : Pour gérer le routage dans l'application React.
- `react-icons` : Pour ajouter des icônes à l'interface utilisateur.

### 4. Configurer MongoDB

Si vous utilisez une instance locale de MongoDB, assurez-vous qu'elle est en cours d'exécution. Sinon, vous pouvez configurer une base de données MongoDB en ligne comme MongoDB Atlas.

Dans votre fichier `database.py`, ajustez les paramètres de connexion à MongoDB :

```python
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')  # Remplacez par votre URI MongoDB
    db = client['appartements']
    return db['annonces']
```

### 5. Lancer le scraper

Le script de scraping peut être exécuté en appelant la fonction `scrape_with_bs4(url)`.

Exemple :

```python
from scraper import scrape_with_bs4

url = 'https://www.thierry-immobilier.fr/fr/locations'
apartments = scrape_with_bs4(url)
```

Cela lancera le processus de scraping et retournera une liste d'annonces immobilières extraites.

### 6. Lancer l'API Flask

L'API Flask vous permet de récupérer les données sauvegardées dans MongoDB.

Exécutez le serveur Flask avec la commande suivante :

```bash
python main.py
```

L'API sera alors disponible sur `http://127.0.0.1:5001/` par défaut.

#### Points de terminaison disponibles :

- **GET /apartments** : Retourne toutes les annonces d'appartements récupérées.
- **GET /apartments/{id}** : Retourne les détails d'un appartement spécifique (par `id`).

### 7. Lancer le frontend React

Dans le dossier `frontend`, démarrez le serveur de développement React avec la commande :

```bash
npm start
```

Le frontend sera alors disponible sur `http://localhost:3000/` par défaut. Il affichera les annonces récupérées via l'API Flask.

## Utilisation de Docker

Pour faciliter l'exécution de ce projet dans un environnement conteneurisé, nous avons préparé une configuration Docker. Cela permet de lancer à la fois l'application Flask, le frontend React, et MongoDB dans des conteneurs isolés.

### 1. Créer une image Docker

Dans le dossier racine du projet, créez un fichier `Dockerfile` pour l'application Flask :

```dockerfile
# Utilisation d'une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'API Flask
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "main.py"]
```

### 2. Docker pour React

Dans le dossier `frontend`, créez un fichier `Dockerfile` pour le frontend React :

```dockerfile
# Utilisation d'une image Node.js officielle
FROM node:16-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application React
COPY . /app

# Installer les dépendances
RUN npm install

# Exposer le port de l'application React
EXPOSE 3000

# Commande pour démarrer l'application
CMD ["npm", "start"]
```

### 3. Lancer MongoDB avec Docker

MongoDB peut être exécuté dans un conteneur Docker. Voici une commande pour démarrer MongoDB dans un conteneur :

```bash
docker run --name mongodb -d -p 27017:27017 mongo:latest
```

Cela lance MongoDB sur le port `27017` de votre machine locale.

### 4. Construire et démarrer l'application avec Docker Compose

Nous vous recommandons d'utiliser `docker-compose` pour simplifier le processus. Voici un fichier `docker-compose.yml` pour orchestrer MongoDB, l'application Flask et le frontend React :

```yaml
version: '3'

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    depends_on:
      - mongodb

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    depends_on:
      - backend

  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
```

### 5. Démarrer les conteneurs

Avec Docker Compose, vous pouvez démarrer tous les services nécessaires (MongoDB, l'API Flask, et le frontend React) en une seule commande :

```bash
docker-compose up --build
```

Cela construira et lancera les trois conteneurs : un pour l'application Flask, un pour MongoDB, et un pour React. L'API Flask sera disponible à l'adresse `http://localhost:5000/` et le frontend React à `http://localhost:3000/`.

## Architecture

### Fichiers principaux :

- **`main.py`** : Contient l'API Flask qui expose les données récupérées.
- **`scraper.py`** : Contient les fonctions pour scraper les données du site web.
- **`database.py`** : Contient la fonction pour se connecter à MongoDB et y stocker les données.
- **`requirements.txt`** : Liste des dépendances Python nécessaires pour faire fonctionner le projet.
- **`Dockerfile`** : Fichier pour construire l'image Docker de l'application Flask.
- **`frontend/Dockerfile`** : Fichier pour construire l'image Docker du frontend React.
- **`docker-compose.yml`** : Fichier de configuration Docker Compose pour orchestrer MongoDB, l'application Flask et le

 frontend React.

## Conclusion

Ce projet fournit une solution complète pour le scraping d'annonces immobilières, avec un backend Flask, un frontend React et une base de données MongoDB. Grâce à Docker, l'ensemble du projet peut être facilement conteneurisé et déployé sur n'importe quelle machine.

Si vous avez des questions, n'hésitez pas à consulter la documentation ou à ouvrir une issue sur le dépôt GitHub.

---

Mathéo DELAUNAY
```

Cela inclut des instructions pour démarrer avec Docker, ainsi que des détails sur le frontend React.