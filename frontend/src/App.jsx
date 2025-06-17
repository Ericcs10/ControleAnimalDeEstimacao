import { useState } from 'react';
import UserForm from './components/UserForm';
import UserTable from './components/UserTable';

function App() {
  const [refresh, setRefresh] = useState(0);

  const refreshUsers = () => setRefresh((prev) => prev + 1);

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-purple-700 text-white w-full py-5 text-center text-2xl font-bold shadow-md">
        Controle de Animais
      </header>

      <main className="flex flex-col items-center justify-center px-5 py-10">
        <div className="flex flex-col md:flex-row gap-10 w-full max-w-6xl">
          <UserForm fetchUsers={refreshUsers} />
          <UserTable fetchTrigger={refresh} />
        </div>
      </main>
    </div>
  );
}

export default App;
