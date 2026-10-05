from fastapi import FastAPI
from routes.estudiantes import router
from repositories.estudiante_repository import inicializar

app = FastAPI(title="Sistema Académico - Taller de Observabilidad")

inicializar()

app.include_router(router)

@app.get("/")
def inicio():
    return {"mensaje": "Sistema académico activo"}