import { useEffect, useState } from 'react';
import api from '../services/api';

export default function UserTable({ fetchTrigger }) {
    const [users, setUsers] = useState([]);

    const fetchUsers = async () => {
        const res = await api.get('/usuario/');
        setUsers(res.data);
    };

    const handleDelete = async (id) => {
        await api.delete(`/usuario/${id}`);
        fetchUsers();
    };

    useEffect(() => {
        fetchUsers();
    }, [fetchTrigger]);

    return (
        <div className="bg-white p-6 rounded-xl shadow-md flex-1">
            <h2 className="text-xl font-bold mb-4">Usuários Cadastrados</h2>
            <table className="w-full border-collapse">
                <thead>
                    <tr className="bg-gray-100">
                        <th className="border p-2">Email</th>
                        <th className="border p-2">CPF</th>
                        <th className="border p-2">Telefone</th>
                        <th className="border p-2">Ações</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map(u => (
                        <tr key={u._id} className="hover:bg-gray-50">
                            <td className="border p-2">{u.email}</td>
                            <td className="border p-2">{u.cpf}</td>
                            <td className="border p-2">{u.telefone}</td>
                            <td className="border p-2">
                                <button
                                    onClick={() => handleDelete(u._id)}
                                    className="text-red-600 hover:underline"
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
