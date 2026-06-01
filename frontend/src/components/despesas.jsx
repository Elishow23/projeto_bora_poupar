import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';

export default function despesas() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ descricao: '', valor: '', categoria: 'Fixa', data: '' });

  const handleSalvar = async (e) => {
    e.preventDefault();
    const resposta = await fetch('http://127.0.0.1:8000/despesa/cadastro/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    });

    if (resposta.ok) {
      navigate('/'); // Redireciona o usuário de volta para o Histórico automaticamente
    }
  };

  return (
    <div>
      <header>
        <h2>Adicionar Nova Despesa</h2>
        <Link to="/">⬅️ Voltar para o Histórico</Link>
      </header>

      <form onSubmit={handleSalvar} className="form-despesa">
        <label>Descrição</label>
        <input type="text" required value={form.descricao} onChange={e => setForm({...form, descricao: e.target.value})} />

        <label>Valor (R$)</label>
        <input type="number" step="0.01" required value={form.valor} onChange={e => setForm({...form, valor: e.target.value})} />

        <label>Categoria</label>
        <select value={form.categoria} onChange={e => setForm({...form, categoria: e.target.value})}>
          <option value="Fixa">Fixa</option>
          <option value="Variavel">Variável</option>
          <option value="Essencial">Essencial</option>
          <option value="Diario">Diário</option>
        </select>

        <label>Data</label>
        <input type="date" required value={form.data} onChange={e => setForm({...form, data: e.target.value})} />

        <button type="submit">Salvas Despesa</button>
      </form>
    </div>
  );
}