from pymongo import MongoClient

def delete_all_apartments():
    # Connectez-vous à MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['real_estate']  # Remplacez par le nom de votre base
    collection = db['apartments']  # Remplacez par le nom de votre collection

    # Supprimez tous les documents de la collection
    result = collection.delete_many({})
    
    # Affichez le nombre de documents supprimés pour vérifier
    print(f"{result.deleted_count} documents supprimés.")
