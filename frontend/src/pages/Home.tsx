import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DeleteButton from '../components/DeleteButton.tsx';
import ScrapeButton from '../components/ScrapeButton.tsx';

interface Apartment {
  title: string;
  price: string;
  location: string;
  link: string;
  image_url?: string;
}

const Home: React.FC = () => {
  const [apartments, setApartments] = useState<Apartment[]>([]);

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
    <div className="container mx-auto p-4">
      <div className="flex justify-between mb-6">
        <ScrapeButton />
        <DeleteButton />
      </div>
      <h2 className="text-2xl font-semibold text-gray-700 mb-4">Liste des Appartements</h2>
      <ul className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {apartments.length === 0 && <p>Aucun appartement trouvé</p>}
        {apartments.map((apartment, index) => (
          <li key={index} className="bg-white p-4 rounded shadow">
            <h3 className="text-xl font-bold text-gray-800">{apartment.title}</h3>
            <p className="text-gray-600">Prix: {apartment.price}</p>
            <p className="text-gray-600">Localisation: {apartment.location}</p>
            <a href={apartment.link} className="text-blue-500 hover:underline">
              Détails
            </a>
            {apartment.image_url && (
              <img
                src={apartment.image_url}
                alt={apartment.title}
                className="mt-4 rounded"
              />
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
