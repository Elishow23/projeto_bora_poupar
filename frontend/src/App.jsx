import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Importa o componente com a primeira letra MAIÚSCULA
import DashboardLayout from './components/dashboard';

import HistoricoPage from './components/historico';
import CadastroPage from './components/despesas';
import RelatorioPage from './components/relatorio';

function App() {
  return (
    <Router>
      <Routes>
        {/* Atenção aqui: o elemento precisa começar com letra MAIÚSCULA! */}
        <Route path="/" element={<DashboardLayout />}>
          <Route index element={<HistoricoPage />} />
          <Route path="cadastro" element={<CadastroPage />} />
          <Route path="relatorio" element={<RelatorioPage />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;