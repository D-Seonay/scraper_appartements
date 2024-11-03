from scraper import scrape_with_bs4, save_apartments, display_apartments


# Exemple d'utilisation
apartments = scrape_with_bs4('https://www.thierry-immobilier.fr/fr/locations')  # Appel de la fonction de scraping
save_apartments(apartments)  # Sauvegarde des données dans MongoDB
display_apartments()          # Affichage des données
