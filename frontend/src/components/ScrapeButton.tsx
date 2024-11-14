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
      style={{
        backgroundColor: '#00ffee',
        color: '#fff',
        padding: '10px 20px',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
      }}
    >
      Scraper les données
    </button>
  );
};

export default ScrapeButton;
