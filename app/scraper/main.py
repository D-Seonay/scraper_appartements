from flask import Flask, jsonify
from scraper import scrape_with_bs4, save_apartments, get_apartments
from delete_all_apartments import delete_all_apartments
from flask_cors import CORS
from database import get_db

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = 'https://www.thierry-immobilier.fr/fr/locations'
    apartments = scrape_with_bs4(url)
    save_apartments(apartments)
    return jsonify({'message': 'Données récupérées et sauvegardées', 'apartments': apartments})

@app.route('/apartments', methods=['GET'])
def apartments():
    apartments = get_apartments()
    return jsonify(apartments)

@app.route('/delete', methods=['GET'])
def delete():
    apartments = get_apartments()
    if apartments:
        collection = get_db()
        collection.delete_many({})
        return jsonify({'message': 'Données supprimées'})
    return jsonify({'message': 'Aucune donnée à supprimer'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
