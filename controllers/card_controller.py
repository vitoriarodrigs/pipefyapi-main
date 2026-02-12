from fastapi import APIRouter
from schemas.schemas import PessoaCreate
from services import card_service

router = APIRouter(prefix="/card", tags=["card"])

@router.post("")
def create_card(pessoa: PessoaCreate):
    return card_service.create_card(pessoa)

@router.delete("/{card_id}")
def delete_card(card_id: int):
    return card_service.delete_card(card_id)

@router.post("/{card_id}/move/{phase_id}")
def move_card(card_id: int, phase_id: str):
    return card_service.move_card(card_id, phase_id)