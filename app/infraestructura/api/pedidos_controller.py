from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()
db_pedidos: List[dict] = []


class Pedido(BaseModel):
    idpedido: Optional[int] = None
    producto: str
    cantidad: int


def _find_index(idpedido: int):
    for i, item in enumerate(db_pedidos):
        if item.get("idpedido") == idpedido:
            return i
    return None


@router.post("/", status_code=201)
async def crear_pedido(p: Pedido):
    if p.idpedido is None:
        next_id = max((item.get("idpedido", 0) for item in db_pedidos), default=0) + 1
        p.idpedido = next_id
    db_pedidos.append(p.dict())
    return p


@router.get("/", response_model=List[Pedido])
async def listar_pedidos():
    return [Pedido(**item) for item in db_pedidos]


@router.get("/{idpedido}")
async def leer_pedido(idpedido: int):
    idx = _find_index(idpedido)
    if idx is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return db_pedidos[idx]


@router.delete("/{idpedido}", status_code=204)
async def eliminar_pedido(idpedido: int):
    idx = _find_index(idpedido)
    if idx is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    db_pedidos.pop(idx)
    return None
