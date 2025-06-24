const UsuarioTable = ({ usuarios, aoEditar, aoDeletar }) => {
    return (
        <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-4">Usuários Cadastrados</h2>
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
                    {usuarios.length === 0 ? (
                        <tr>
                            <td colSpan="4" className="text-center p-2">
                                Nenhum usuário cadastrado
                            </td>
                        </tr>
                    ) : (
                        usuarios.map((usuario) => (
                            <tr key={usuario._id}>
                                <td className="border p-2">{usuario.email}</td>
                                <td className="border p-2">{usuario.cpf}</td>
                                <td className="border p-2">{usuario.telefone}</td>
                                <td className="border p-2 flex gap-2 justify-center">
                                    <button
                                        onClick={() => aoEditar(usuario)}
                                        className="bg-blue-500 text-white px-2 rounded"
                                    >
                                        ✏️
                                    </button>
                                    <button
                                        onClick={() => aoDeletar(usuario._id)}
                                        className="bg-red-500 text-white px-2 rounded"
                                    >
                                        🗑️
                                    </button>
                                </td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default UsuarioTable;
