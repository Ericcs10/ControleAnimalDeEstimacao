import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import random 
from app.core.config import settings

# Enums
ESPECIES = ["Canino", "Felino", "Ave", "Roedor"]
SEXOS = ["Masculino", "Feminino", "Outro"]
INTERVALOS = ["Dias", "Meses", "Anos"]

# MongoDB client usando configuração
client = AsyncIOMotorClient(settings.mongodb_url, uuidRepresentation="standard")
db = client[settings.mongodb_name]

async def popular_dados(limpar_db=True):
    if limpar_db:
        print("🗑️ Limpando base...")
        await db.usuarios.delete_many({})
        await db.racas.delete_many({})
        await db.animais_estimacao.delete_many({})
        await db.vacinas.delete_many({})

    print("🚀 Inserindo dados...")

    # Criar raças
    racas = []
    for i in range(3):
        raca = {
            "tipo": f"Raça {i}",
            "pelagem": random.choice(["Curta", "Longa", "Média"]),
            "tamanho_pelagem": random.choice(["Pequeno", "Grande"]),
            "temperamento": random.choice(["Calmo", "Agressivo", "Sociável"]),
            "especie": random.choice(ESPECIES)
        }
        raca_id = await db.racas.insert_one(raca)
        racas.append(raca_id.inserted_id)

    # Criar usuários
    usuarios = []
    for i in range(2):
        usuario = {
            "email": f"user{i}@email.com",
            "cpf": f"0000000000{i}",
            "telefone": f"6199999999{i}",
            "senha_hash": "123456_hashed",
            "data_criacao": datetime.utcnow(),
            "data_atualizacao": datetime.utcnow()
        }
        usuario_id = await db.usuarios.insert_one(usuario)
        usuarios.append(usuario_id.inserted_id)

    # Criar animais
    animais = []
    for i in range(3):
        animal = {
            "usuario_id": random.choice(usuarios),
            "especie": random.choice(ESPECIES),
            "raca": random.choice(racas),
            "nome": f"Pet_{i}",
            "data_nascimento": datetime(2021, random.randint(1, 12), random.randint(1, 28)),
            "sexo": random.choice(SEXOS),
            "data_criacao": datetime.utcnow(),
            "data_atualizacao": datetime.utcnow()
        }
        animal_id = await db.animais_estimacao.insert_one(animal)
        animais.append(animal_id.inserted_id)

    # Criar vacinas
    for i in range(5):
        data_vacina = datetime.utcnow() - timedelta(days=random.randint(30, 365))
        vacina = {
            "animal_id": random.choice(animais),
            "nome": f"Vacina {i}",
            "data": data_vacina,
            "lote": f"Lote{i}",
            "laboratorio": "LabXYZ",
            "necessita_revacina": True,
            "periodo": 12,
            "intervalo": random.choice(INTERVALOS),
            "proxima_dose": data_vacina + timedelta(days=365)
        }
        await db.vacinas.insert_one(vacina)

    print("✅ Dados fake inseridos com sucesso.")

if __name__ == "__main__":
    asyncio.run(popular_dados())
