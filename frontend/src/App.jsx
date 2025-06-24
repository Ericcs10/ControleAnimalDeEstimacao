import { useEffect, useState } from "react";
import {
  listarUsuarios,
  criarUsuario,
  atualizarUsuario,
  deletarUsuario,
} from "./services/usuarioService";
import UsuarioForm from "./components/UsuarioForm";
import UsuarioTable from "./components/UsuarioTable";

function App() {
  const [usuarios, setUsuarios] = useState([]);
  const [usuarioEditando, setUsuarioEditando] = useState(null);

  const carregarUsuarios = async () => {
    const dados = await listarUsuarios();
    setUsuarios(dados);
  };

  useEffect(() => {
    carregarUsuarios();
  }, []);

  const handleSalvar = async (usuario) => {
    try {
      if (usuarioEditando) {
        await atualizarUsuario(usuarioEditando._id, usuario);
        setUsuarioEditando(null);
      } else {
        await criarUsuario(usuario);
      }
      carregarUsuarios();
    } catch (error) {
      alert("Erro ao salvar usuário");
    }
  };

  const handleDeletar = async (id) => {
    try {
      await deletarUsuario(id);
      carregarUsuarios();
    } catch (error) {
      alert("Erro ao deletar usuário");
    }
  };

  const handleEditar = (usuario) => {
    setUsuarioEditando(usuario);
  };

  return (
    <div className="p-4 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold text-center mb-4 text-purple-800">
        Controle de Animais
      </h1>
      <div className="flex gap-4 justify-center">
        <UsuarioForm aoSalvar={handleSalvar} usuarioAtual={usuarioEditando} />
        <UsuarioTable
          usuarios={usuarios}
          aoEditar={handleEditar}
          aoDeletar={handleDeletar}
        />
      </div>
    </div>
  );
}

export default App;
