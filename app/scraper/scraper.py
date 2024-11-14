import requests
from bs4 import BeautifulSoup
from database import get_db
from datetime import datetime

def scrape_with_bs4(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    # Vérification de la réponse
    if response.status_code != 200:
        print(f"Erreur lors de la requête : {response.status_code}")
        return []

    # Analyse du contenu
    soup = BeautifulSoup(response.content, 'html.parser')
    apartments = []

    # Boucle sur chaque annonce
    for offer in soup.find_all('div', class_='article'):
        # Récupérer le titre
        title_tag = offer.find('h3')
        title = title_tag.text.strip() if title_tag else "N/A"

        # Récupérer le prix
        price_tag = offer.find('span', class_='prix')
        price = price_tag.text.strip() if price_tag else "N/A"

        # Récupérer la localisation
        location_tag = title_tag.find_all('br')
        location = location_tag[-1].previous_sibling.strip() if location_tag else "N/A"

        # Récupérer le lien de l'annonce
        link_tag = offer.find('a', href=True)
        link = 'https://www.thierry-immobilier.fr' + link_tag['href'] if link_tag else "N/A"

        # Récupérer l'URL de l'image
        img_tag = offer.find('img')
        image_url = img_tag['src'] if img_tag else "N/A"

        # Date et heure du scraping (formatée en UTC)
        scrapped_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Ajouter les données extraites dans la liste avec la date et l'heure actuelles
        apartments.append({
            'title': title,
            'price': price,
            'location': location,
            'link': link,
            'image_url': image_url,
            'scraped_at': scrapped_at  # Cette ligne assure que la clé existe
        })

    print(f"Appartements récupérés : {apartments}")
    return apartments  # Retourne les appartements

def save_apartments(apartments):
    collection = get_db()  # Récupérer la collection
    if apartments:
        try:
            # Vous pouvez vérifier s'il existe déjà un appartement avec le même lien pour éviter les doublons
            for apartment in apartments:
                if collection.find_one({'link': apartment['link']}):
                    print(f"Appartement déjà présent : {apartment['title']}")
                    continue
                collection.insert_one(apartment)  # Utilisation de insert_one pour insérer chaque appartement individuellement
            print("Données sauvegardées dans MongoDB")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde dans MongoDB : {e}")
    else:
        print("Aucune donnée à sauvegarder.")

def get_apartments():
    collection = get_db()  # Récupérer la collection
    apartments = list(collection.find())  # Récupère tous les appartements
    return [{
        'title': apartment.get('title', 'N/A'),
        'price': apartment.get('price', 'N/A'),
        'location': apartment.get('location', 'N/A'),
        'link': apartment.get('link', 'N/A'),
        'image_url': apartment.get('image_url', 'N/A'),
        'scraped_at': apartment.get('scraped_at', 'N/A') 
    } for apartment in apartments]


def get_dataBase():
    collection = get_db()  # Récupérer la collection
    apartments = list(collection.find())  # Récupère tous les appartements
    return apartments
