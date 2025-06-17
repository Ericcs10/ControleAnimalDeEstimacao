import { useState } from 'react';
import api from '../services/api';

export default function UserForm({ fetchUsers }) {
    const [formData, setFormData] = useState({
        email: '',
        cpf: '',
        telefone: '',
        senha: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await api.post('/usuario/', formData);
        setFormData({ email: '', cpf: '', telefone: '', senha: '' });
        fetchUsers();
    };

    return (
        <div className="bg-white p-6 rounded-xl shadow-md flex-1">
            <h2 className="text-xl font-bold mb-4">Cadastrar novo usuário</h2>
            <form onSubmit={handleSubmit} className="flex flex-col">
                <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} className="input" required />
                <input type="text" name="cpf" placeholder="CPF" value={formData.cpf} onChange={handleChange} className="input" required />
                <input type="text" name="telefone" placeholder="Telefone" value={formData.telefone} onChange={handleChange} className="input" required />
                <input type="password" name="senha" placeholder="Senha" value={formData.senha} onChange={handleChange} className="input" required />
                <button type="submit" className="button">Cadastrar</button>
            </form>
        </div>
    );
}
