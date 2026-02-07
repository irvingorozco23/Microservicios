from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    idusuario: Optional[int] = None
    nombre: str
    email: str