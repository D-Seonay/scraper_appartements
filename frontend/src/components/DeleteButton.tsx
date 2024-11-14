import React from 'react';
import axios from 'axios';

const DeleteButton: React.FC = () => {
  const handleDelete = async () => {
    try {
      const response = await axios.get('http://localhost:5001/delete');
      window.location.reload();
    } catch (error) {
      console.error('Erreur lors de la suppression des données', error);
      alert("Échec de la suppression des données.");
    }
  };

  return (
    <button
      onClick={handleDelete}
      className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-400 focus:ring-opacity-50 transition-colors duration-300"
    >
      Supprimer les données
    </button>
  );
};

export default DeleteButton;
