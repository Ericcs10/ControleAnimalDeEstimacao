import { useState, useEffect } from "react";

const UsuarioForm = ({ aoSalvar, usuarioAtual }) => {
    const [email, setEmail] = useState("");
    const [cpf, setCpf] = useState("");
    const [telefone, setTelefone] = useState("");
    const [senha, setSenha] = useState("");

    useEffect(() => {
        if (usuarioAtual) {
            setEmail(usuarioAtual.email);
            setCpf(usuarioAtual.cpf);
            setTelefone(usuarioAtual.telefone);
            setSenha(usuarioAtual.senha);
        }
    }, [usuarioAtual]);

    const handleSubmit = (e) => {
        e.preventDefault();
        aoSalvar({
            email,
            cpf,
            telefone,
            senha,
        });
        setEmail("");
        setCpf("");
        setTelefone("");
        setSenha("");
    };

    return (
        <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-4">Cadastrar novo usuário</h2>
            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="border p-2 mb-2 w-full"
                required
            />
            <input
                type="text"
                placeholder="CPF"
                value={cpf}
                onChange={(e) => setCpf(e.target.value)}
                className="border p-2 mb-2 w-full"
                required
            />
            <input
                type="text"
                placeholder="Telefone"
                value={telefone}
                onChange={(e) => setTelefone(e.target.value)}
                className="border p-2 mb-2 w-full"
                required
            />
            <input
                type="password"
                placeholder="Senha"
                value={senha}
                onChange={(e) => setSenha(e.target.value)}
                className="border p-2 mb-4 w-full"
                required
            />
            <button className="bg-purple-700 text-white px-4 py-2 rounded">
                {usuarioAtual ? "Atualizar" : "Cadastrar"}
            </button>
        </form>
    );
};

export default UsuarioForm;
