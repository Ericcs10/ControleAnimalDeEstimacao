from app.models.especie_model import Especie
from app.repositories import especie_repository

def criar_especie(nome: str):
    especie = Especie(nome=nome)
    especie_id = especie_repository.create_especie(especie)
    return str(especie_id)

def listar_especies():
    return especie_repository.get_all_especies()

def buscar_especie_por_id(especie_id: str):
    return especie_repository.get_especie_by_id(especie_id)

def atualizar_especie(especie_id: str, nome: str):
    return especie_repository.update_especie(especie_id, nome)

def deletar_especie(especie_id: str):
    return especie_repository.delete_especie(especie_id)
