import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home.tsx';
import Navbar from './components/Navbar.tsx';
const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="min-h-screen bg-gray-100 p-6">
        <h1 className="text-4xl font-bold text-center text-gray-800 mb-8">Gestion des Appartements</h1>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="*" element={<h1>404 - Not Found</h1>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
