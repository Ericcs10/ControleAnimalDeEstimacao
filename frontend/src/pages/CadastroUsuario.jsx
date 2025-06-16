import { useState, useEffect } from 'react';
import api from '../services/api';

export default function CadastroUsuario() {
    const [usuarios, setUsuarios] = useState([]);
    const [form, setForm] = useState({
        email: '',
        cpf: '',
        telefone: '',
        senha: '',
    });

    useEffect(() => {
        carregarUsuarios();
    }, []);

    const carregarUsuarios = async () => {
        const res = await api.get('/usuarios/');
        setUsuarios(res.data);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await api.post('/usuarios/', form);
        setForm({ email: '', cpf: '', telefone: '', senha: '' });
        carregarUsuarios();
    };

    const handleDelete = async (id) => {
        await api.delete(`/usuarios/${id}`);
        carregarUsuarios();
    };

    return (
        <div className="max-w-2xl mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Cadastro de Usuário</h1>

            <form onSubmit={handleSubmit} className="space-y-3 mb-6">
                <input
                    type="email"
                    placeholder="Email"
                    value={form.email}
                    onChange={(e) => setForm({ ...form, email: e.target.value })}
                    className="border px-3 py-2 w-full"
                    required
                />
                <input
                    type="text"
                    placeholder="CPF"
                    value={form.cpf}
                    onChange={(e) => setForm({ ...form, cpf: e.target.value })}
                    className="border px-3 py-2 w-full"
                    required
                />
                <input
                    type="text"
                    placeholder="Telefone"
                    value={form.telefone}
                    onChange={(e) => setForm({ ...form, telefone: e.target.value })}
                    className="border px-3 py-2 w-full"
                    required
                />
                <input
                    type="password"
                    placeholder="Senha"
                    value={form.senha}
                    onChange={(e) => setForm({ ...form, senha: e.target.value })}
                    className="border px-3 py-2 w-full"
                    required
                />
                <button className="bg-blue-600 text-white px-4 py-2 rounded">
                    Cadastrar
                </button>
            </form>

            <h2 className="text-xl font-semibold mb-2">Usuários Cadastrados</h2>
            <table className="w-full border">
                <thead>
                    <tr className="bg-gray-100">
                        <th className="border p-2">Email</th>
                        <th className="border p-2">CPF</th>
                        <th className="border p-2">Telefone</th>
                        <th className="border p-2">Ações</th>
                    </tr>
                </thead>
                <tbody>
                    {usuarios.map((u) => (
                        <tr key={u.id}>
                            <td className="border p-2">{u.email}</td>
                            <td className="border p-2">{u.cpf}</td>
                            <td className="border p-2">{u.telefone}</td>
                            <td className="border p-2">
                                <button
                                    onClick={() => handleDelete(u.id)}
                                    className="bg-red-600 text-white px-2 py-1 rounded"
                                >
                                    Excluir
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
