from pymongo import MongoClient

# Configuration MongoDB
def get_db():
    client = MongoClient('mongodb://mongo:27017/')  # Nom du service MongoDB défini dans docker-compose
    db = client['real_estate']  # Nom de la base de données
    return db['apartments']  # Nom de la collection
