import React from 'react';
import { Link, Outlet, useLocation } from 'react-router-dom';

export default function dashboard() {
  const location = useLocation();

  // Função simples para destacar a página onde o usuário está clicado
  const linkAtivo = (path) => {
    return location.pathname === path 
      ? "bg-slate-800 text-emerald-400 font-bold border-l-4 border-emerald-500 pl-3" 
      : "text-slate-400 hover:text-slate-200 hover:bg-slate-900/50 pl-4";
  };

  return (
    <div className="flex min-h-screen bg-slate-950 text-slate-100 antialiased font-sans">
      
      {/* BARRA LATERAL (SIDEBAR) FIXA */}
      <aside className="w-64 bg-slate-900/60 border-r border-slate-800/60 backdrop-blur-md flex flex-col justify-between p-6 sticky top-0 h-screen">
        <div className="space-y-8">
          {/* Logo do Sistema */}
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-tr from-emerald-500 to-teal-400 p-2 rounded-xl shadow-lg shadow-emerald-500/10">
              <span className="text-xl text-slate-950 font-bold">⚡</span>
            </div>
            <span className="text-base font-black tracking-wider bg-gradient-to-r from-emerald-400 to-teal-300 bg-clip-text text-transparent">
              BORA POUPAR
            </span>
          </div>

          {/* Links de Navegação */}
          <nav className="flex flex-col gap-2 text-sm">
            <p className="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2 px-4">Menu Principal</p>
            
            <Link to="/" className={`flex items-center py-2.5 rounded-xl transition duration-200 ${linkAtivo('/')}`}>
              <span className="mr-3">📋</span> Histórico
            </Link>
            
            <Link to="/cadastro" className={`flex items-center py-2.5 rounded-xl transition duration-200 ${linkAtivo('/cadastro')}`}>
              <span className="mr-3">➕</span> Novo Lançamento
            </Link>
            
            <Link to="/relatorio" className={`flex items-center py-2.5 rounded-xl transition duration-200 ${linkAtivo('/relatorio')}`}>
              <span className="mr-3"> Bars 📊</span> Relatório
            </Link>
          </nav>
        </div>

        {/* Status do Servidor no Rodapé da Barra Lateral */}
        <div className="bg-slate-950/60 border border-slate-800 px-4 py-2.5 rounded-xl flex items-center gap-3 shadow-inner">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span className="text-[10px] font-bold tracking-wide uppercase text-slate-400">Django Conectado</span>
        </div>
      </aside>

      {/* ÁREA DE CONTEÚDO DA DIREITA */}
      <div className="flex-1 flex flex-col min-w-0">
        
        {/* BARRA SUPERIOR DE CONTEXTO */}
        <header className="h-16 border-b border-slate-800/60 bg-slate-900/20 backdrop-blur-md px-8 flex items-center justify-end text-xs text-slate-400">
          <span>Usuário: <strong className="text-slate-200">Eliseu Cosme</strong></span>
        </header>

        {/* ESPAÇO ONDE A PÁGINA ATIVA SERÁ RENDERIZADA */}
        <main className="flex-1 p-8 max-w-5xl w-full mx-auto">
          <Outlet />
        </main>
      </div>

    </div>
  );
}