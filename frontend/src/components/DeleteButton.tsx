import React from 'react';
import axios from 'axios';

const DeleteButton: React.FC = () => {
  const handleDelete = async () => {
    try {
      const response = await axios.get('http://localhost:5001/delete');
      alert(response.data.message);
    } catch (error) {
      console.error('Erreur lors de la suppression des données', error);
      alert("Échec de la suppression des données.");
    }
  };

  return (
    <button
      onClick={handleDelete}
      style={{
        backgroundColor: '#ff4d4f',
        color: '#fff',
        padding: '10px 20px',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
      }}
    >
      Supprimer les données
    </button>
  );
};

export default DeleteButton;
