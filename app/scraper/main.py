from flask import Flask, jsonify
from scraper import scrape_with_bs4, save_apartments, get_apartments
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})  # Autoriser toutes les origines

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
