from fastapi import FastAPI
from routers import atleta, categoria, centro_treinamento

app = FastAPI(
    title="Workout API",
    version="0.1.0"
)

app.include_router(atleta.router)
app.include_router(categoria.router)
app.include_router(centro_treinamento.router)
