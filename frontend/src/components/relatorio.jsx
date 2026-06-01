import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function relatorio() {
  const [dados, setDados] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/despesa/relatorio/')
      .then(res => res.json())
      .then(data => setDados(data));
  }, []);

  return (
    <div>
      <header>
        <h2>Relatório de Gastos por Categoria</h2>
        <Link to="/">⬅️ Voltar para o Histórico</Link>
      </header>

      <main>
        <div>
          {dados.map((item, idx) => (
            <div key={idx} style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
              <strong>{item.categoria}: </strong>
              <span>R$ {item.total.toFixed(2)}</span>
            </div>
          ))}
          {dados.length === 0 && <p>Nenhum dado para exibir.</p>}
        </div>
      </main>
    </div>
  );
}