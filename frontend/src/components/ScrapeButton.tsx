import React from 'react';
import axios from 'axios';

const ScrapeButton: React.FC = () => {
  const handleDelete = async () => {
    try {
      const response = await axios.get('http://localhost:5001/scrape');
      alert(response.data.message);
    } catch (error) {
      console.error('Erreur lors du scraping des données', error);
      alert("Échec du scraping des données.");
    }
  };

  return (
    <button
      onClick={handleDelete}
      className="bg-teal-400 text-white px-5 py-2 rounded-lg hover:bg-teal-500 focus:outline-none focus:ring-2 focus:ring-teal-600"
    >
      Scraper les données
    </button>
  );
};

export default ScrapeButton;
