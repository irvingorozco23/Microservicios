from fastapi import APIRouter, HTTPException
from app.domain.core.models import Usuario

router = APIRouter()
db_temporal = [] # Simulación de DB

@router.post("/", status_code=201)
async def crear(u: Usuario):
    db_temporal.append(u)
    return u

@router.get("/{idusuario}")
async def leer(idusuario: int):
    return {"idusuario": idusuario, "nombre": "Irving", "email": "irving@ejemplo.com"}