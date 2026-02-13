from fastapi import FastAPI
from app.infraestructura.api.controller import router as usuarios_router

app = FastAPI(title="Usuarios Service")
app.include_router(usuarios_router, prefix="/usuarios")

@app.get("/")
def root():
    return {"mensaje": "Microservicio Usuarios en puerto 8001"}
