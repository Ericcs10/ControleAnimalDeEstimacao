from app.models.especie_model import Especie
from app.repositories import especie_repository
from app.services.base_service import BaseService

class EspecieService(BaseService[str]):

    async def criar(self, nome: str):
        especie = Especie(nome=nome)
        especie_id = especie_repository.create_especie(especie)
        return str(especie_id)

    async def listar(self):
        return especie_repository.get_all_especies()

    async def buscar_por_id(self, especie_id: str):
        return especie_repository.get_especie_by_id(especie_id)

    async def atualizar(self, especie_id: str, nome: str):
        return especie_repository.update_especie(especie_id, nome)

    async def deletar(self, especie_id: str):
        return especie_repository.delete_especie(especie_id)