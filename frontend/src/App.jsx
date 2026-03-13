import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./paginas/home"
import Despesas from "./paginas/despesas"
import Relatorio from "./paginas/relatorio"

function App() {
  return (
    <BrowserRouter>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/despesas" element={<Despesas />} />
        <Route path="/relatorio" element={<Relatorio />} />
      </Routes>

    </BrowserRouter>
  )
}

export default App

/*function App() {
  const [despesas, setDespesas] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/despesas/")
      .then(res => res.json())
      .then(data => setDespesas(data));
  }, []);

  return (
    <div>
      <h1>Lista de Despesas</h1>

      {despesas.map((d, index) => (
        <p key={index}>
          {d.categoria} - R$ {d.valor}
        </p>
      ))}

    </div>
  );
}

export default App;*/
