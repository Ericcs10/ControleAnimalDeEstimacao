import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;

export const listarUsuarios = async () => {
    const response = await axios.get(`${API_URL}/usuarios/`);
    return response.data;
};

export const criarUsuario = async (usuario) => {
    const response = await axios.post(`${API_URL}/usuarios/`, usuario);
    return response.data;
};

export const deletarUsuario = async (id) => {
    const response = await axios.delete(`${API_URL}/usuarios/${id}`);
    return response.data;
};

export const atualizarUsuario = async (id, usuario) => {
    const response = await axios.put(`${API_URL}/usuarios/${id}`, usuario);
    return response.data;
};
