from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse
from typing import List
from io import BytesIO

from app.schemas.animal_schema import AnimalCreate, AnimalUpdate, AnimalRead
from app.services.animal_service import AnimalService
from app.repositories.vacina_repository import VacinaRepository
from app.utils.pdf_generator import gerar_pdf_animal

router = APIRouter(prefix="/animais", tags=["Animais"]) 
service = AnimalService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
async def criar_animal(animal: AnimalCreate):
    animal_id = await service.criar(animal)
    return {"id": animal_id}


@router.get("/", response_model=List[AnimalRead])
async def listar_animais():
    return await service.listar()


@router.get("/{animal_id}", response_model=AnimalRead)
async def buscar_animal(animal_id: str):
    animal = await service.buscar_por_id(animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal


@router.put("/{animal_id}", response_model=dict)
async def atualizar_animal(animal_id: str, dados: AnimalUpdate):
    sucesso = await service.atualizar(animal_id, dados)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Animal não encontrado ou nada foi alterado")
    return {"message": "Animal atualizado com sucesso"}


@router.delete("/{animal_id}", response_model=dict)
async def deletar_animal(animal_id: str):
    sucesso = await service.deletar(animal_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return {"message": "Animal removido com sucesso"}


@router.get("/{animal_id}/pdf")
async def gerar_pdf(animal_id: str):
    animal = await service.buscar_por_id(animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")

    vacinas = await VacinaRepository.listar_por_animal(animal_id)
    pdf_bytes = gerar_pdf_animal(animal, vacinas)

    return StreamingResponse(
        BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f"inline; filename=animal_{animal_id}.pdf"}
    )
