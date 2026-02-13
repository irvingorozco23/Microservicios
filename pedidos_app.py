from fastapi import FastAPI
from app.infraestructura.api.pedidos_controller import router as pedidos_router

app = FastAPI(title="Pedidos Service")
app.include_router(pedidos_router, prefix="/pedidos")

@app.get("/")
def root():
    return {"mensaje": "Microservicio Pedidos en puerto 8002"}
