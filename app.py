from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Route principale pour afficher les appartements
@app.route('/')
def show_apartments():
    # Lire les données depuis le fichier CSV
    df = pd.read_csv('apartments.csv')
    apartments = df.to_dict(orient='records')  # Convertit les données en liste de dictionnaires
    return render_template('apartments.html', apartments=apartments)

if __name__ == '__main__':
    app.run(debug=True)
