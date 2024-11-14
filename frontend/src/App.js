import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DeleteButton from './components/DeleteButton.tsx';
import ScrapeButton from './components/ScrapeButton.tsx';

const App = () => {
  const [apartments, setApartments] = useState([]);

  useEffect(() => {
    const fetchApartments = async () => {
      try {
        const response = await axios.get('http://localhost:5001/apartments');
        setApartments(response.data);
      } catch (error) {
        console.error('Erreur lors de la récupération des appartements', error);
      }
    };

    fetchApartments();
  }, []);

  return (
    <div>
      <h1>Liste des AppartementsS</h1>
      <DeleteButton />
      <ScrapeButton />
      <ul>
        {apartments.length === 0 && <p>Aucun appartement trouvé</p>}
        {apartments.map((apartment, index) => (
          <li key={index}>
            <h2>{apartment.title}</h2>
            <p>Prix: {apartment.price}</p>
            <p>Localisation: {apartment.location}</p>
            <a href={apartment.link}>Détails</a>
            {apartment.image_url && <img src={apartment.image_url} alt={apartment.title} />}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
