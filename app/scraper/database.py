from pymongo import MongoClient

# Fonction pour se connecter à la base de données
def get_db():
    client = MongoClient('mongodb://mongo:27017/')  # Assurez-vous que le nom du service MongoDB est correct
    db = client['real_estate']  # Nom de la base de données
    return db['apartments']  # Nom de la collection


# Fonction pour supprimer la base de données
def delete_db():
    client = MongoClient('mongodb://mongo:27017/')  # Assurez-vous que le nom du service MongoDB est correct
    db = client['real_estate']  # Nom de la base de données
    db.drop_collection('apartments')  # Supprimer la collection
    return db['apartments']  # Nom de la collection
