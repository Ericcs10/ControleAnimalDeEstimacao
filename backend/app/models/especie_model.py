from pydantic import BaseModel, Field
from bson import ObjectId

class Especie:
    def __init__(self, nome: str, _id: ObjectId = None):
        self._id = _id or ObjectId()
        self.nome = nome

    def to_dict(self):
        return {
            "_id": self._id,
            "nome": self.nome
        }

    @staticmethod
    def from_dict(data: dict):
        return Especie(
            nome=data["nome"],
            _id=data["_id"]
        )
