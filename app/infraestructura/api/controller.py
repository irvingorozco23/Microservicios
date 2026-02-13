from fastapi import APIRouter, HTTPException
from app.domain.core.models import Usuario
from typing import List

router = APIRouter()
# Simulación de base de datos en memoria (lista de dicts)
db_temporal: List[dict] = []


def _find_index(idusuario: int):
    for i, item in enumerate(db_temporal):
        if item.get("idusuario") == idusuario:
            return i
    return None


@router.post("/", status_code=201)
async def crear(u: Usuario):
    # Asignar id si no viene
    if u.idusuario is None:
        next_id = max((item.get("idusuario", 0) for item in db_temporal), default=0) + 1
        u.idusuario = next_id
    db_temporal.append(u.dict())
    return u


@router.get("/", response_model=List[Usuario])
async def listar():
    return [Usuario(**item) for item in db_temporal]


@router.get("/{idusuario}")
async def leer(idusuario: int):
    idx = _find_index(idusuario)
    if idx is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_temporal[idx]


@router.put("/{idusuario}")
async def actualizar(idusuario: int, u: Usuario):
    idx = _find_index(idusuario)
    if idx is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # mantener el id solicitado
    updated = u.dict()
    updated["idusuario"] = idusuario
    db_temporal[idx] = updated
    return updated


@router.delete("/{idusuario}", status_code=204)
async def eliminar(idusuario: int):
    idx = _find_index(idusuario)
    if idx is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_temporal.pop(idx)
    return None