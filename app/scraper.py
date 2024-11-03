import requests
from bs4 import BeautifulSoup
from database import get_db

# URL du site à scraper
url = 'https://www.thierry-immobilier.fr/fr/locations'

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
    # Boucle sur chaque annonce
    for offer in soup.find_all('div', class_='article'):
        # Récupérer le titre
        title_tag = offer.find('h3')
        title = title_tag.text.strip() if title_tag else "N/A"

        # Récupérer le prix
        price_tag = offer.find('span', class_='prix')
        price = price_tag.text.strip() if price_tag else "N/A"

        # Récupérer la localisation
        location_tag = title_tag.find_all('br')  # Les informations de localisation sont après le titre
        location = location_tag[-1].previous_sibling.strip() if location_tag else "N/A"

        # Récupérer le lien de l'annonce
        link_tag = offer.find('a', href=True)
        link = 'https://www.bienici.com' + link_tag['href'] if link_tag else "N/A"

        # Récupérer l'URL de l'image
        img_tag = offer.find('img')
        image_url = img_tag['src'] if img_tag else "N/A"
        
        # Ajouter les données extraites dans la liste
        apartments.append({
            'title': title,
            'price': price,
            'location': location,
            'link': link,
            'image_url': image_url
        })
    
    # Afficher les appartements récupérés pour déboguer
    print(f"Appartements récupérés : {apartments}")

    return apartments  # Retourne les appartements


def save_apartments(apartments):
    collection = get_db()  # Récupérer la collection
    if apartments:
        collection.insert_many(apartments)
        print("Données sauvegardées dans MongoDB")
    else:
        print("Aucune donnée à sauvegarder." + " " * 40)

def display_apartments():
    collection = get_db()  # Récupérer la collection
    apartments = collection.find()
    for apartment in apartments:
        print(f"Titre: {apartment['title']}")
        print(f"Prix: {apartment['price']}")
        print(f"Localisation: {apartment['location']}")
        print(f"Lien: {apartment['link']}")
        print(f"URL de l'image: {apartment['image_url']}")
        print("-" * 40)