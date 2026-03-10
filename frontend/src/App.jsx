import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


function App() {
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

export default App;
