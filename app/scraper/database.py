from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://mongo:27017/')  # Assurez-vous que le nom du service MongoDB est correct
    db = client['real_estate']  # Nom de la base de données
    return db['apartments']  # Nom de la collection
