import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL des sites à scraper
urls = {
    'site1': 'https://www.exemple.com/recherche/appartement',  # URL d'exemple
    'site2': 'https://www.autresite.com/appartement-a-louer',   # Autre URL
    # Ajoute ici d'autres sites avec les paramètres de recherche si nécessaire
}

# Fonction de scraping pour un site avec BeautifulSoup
def scrape_with_bs4(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    apartments = []

    for offer in soup.find_all('div', class_='offer-class'):  # remplace avec les balises spécifiques du site
        title = offer.find('h2').text.strip()
        price = offer.find('span', class_='price').text.strip()
        location = offer.find('div', class_='location').text.strip()
        link = offer.find('a')['href']
        
        apartments.append({
            'title': title,
            'price': price,
            'location': location,
            'link': link
        })
    
    return apartments

# Fonction de scraping pour un site nécessitant Selenium
def scrape_with_selenium(url):
    driver = webdriver.Chrome()  # Assure-toi d'avoir installé le driver Chrome
    driver.get(url)
    time.sleep(2)  # Laisse le temps au JavaScript de charger

    apartments = []
    offers = driver.find_elements(By.CLASS_NAME, 'offer-class')  # Modifie le sélecteur pour correspondre au site

    for offer in offers:
        title = offer.find_element(By.TAG_NAME, 'h2').text.strip()
        price = offer.find_element(By.CLASS_NAME, 'price').text.strip()
        location = offer.find_element(By.CLASS_NAME, 'location').text.strip()
        link = offer.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        apartments.append({
            'title': title,
            'price': price,
            'location': location,
            'link': link
        })
    
    driver.quit()
    return apartments

# Scraper tous les sites
all_apartments = []

for site, url in urls.items():
    if 'javascript' in url:  # Exemple de condition pour les sites nécessitant Selenium
        all_apartments.extend(scrape_with_selenium(url))
    else:
        all_apartments.extend(scrape_with_bs4(url))

# Exporter les données dans un fichier CSV
df = pd.DataFrame(all_apartments)
df.to_csv('apartments.csv', index=False)
print("Données sauvegardées dans apartments.csv")
