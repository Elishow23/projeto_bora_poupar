import { Link } from "react-router-dom"


function Home() {
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Bem-vindo ao Me Poupe</p>
      <Link to="/despesas">
        <button>Ver Despesas</button>
      </Link>
      <Link to="/relatorio">
        <button>Ver relatorio</button>
      </Link>
    </div>
  )
}

export default Home