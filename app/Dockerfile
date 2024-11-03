# Utiliser une image de base Python
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste de votre code dans le conteneur
COPY ./scraper .

# Exposer le port 5000
EXPOSE 5001

# Commande pour exécuter votre script Python
CMD ["python", "main.py"]
