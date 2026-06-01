import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function historico() {
  const [despesas, setDespesas] = useState([]);
  const [total, setTotal] = useState(0);
  const [busca, setBusca] = useState('');
  const API_URL = 'http://127.0.0.1:8000/despesa/';

  const carregarDados = async () => {
    const resposta = await fetch(API_URL);
    const dados = await resposta.json();
    setDespesas(dados.despesas);
    setTotal(dados.total);
  };

  useEffect(() => { carregarDados(); }, []);

  const handleBuscar = async (e) => {
    const termo = e.target.value;
    setBusca(termo);
    const resposta = await fetch(`${API_URL}pesquisar/?q=${termo}`);
    const dados = await resposta.json();
    setDespesas(dados.despesas);
    setTotal(dados.total);
  };

  const handleExcluir = async (id) => {
    if (window.confirm("Deseja excluir?")) {
      await fetch(`${API_URL}excluir/${id}/`, { method: 'DELETE' });
      carregarDados();
    }
  };

  return (
    <div>
      <header>
        <h1>Histórico de Despesas</h1>
        <nav>
          <Link to="/cadastro">➕ Novo Lançamento</Link> | <Link to="/relatorio">📊 Ver Relatório</Link>
        </nav>
      </header>

      <main>
        <input type="text" placeholder="Pesquisar..." value={busca} onChange={handleBuscar} />

        <div className="lista-despesas">
          {despesas.map(d => (
            <div className="card" key={d.id}>
              <h3>{d.descricao}</h3>
              <p>R$ {d.valor}</p>
              <small>{d.categoria} | {d.data}</small>
              <button onClick={() => handleExcluir(d.id)}>🗑️ Excluir</button>
            </div>
          ))}
        </div>

        <div>
          <h3>Total: R$ {total.toFixed(2)}</h3>
        </div>
      </main>
    </div>
  );
}