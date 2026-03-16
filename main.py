from fastapi import FastAPI
from routers import analistas, chamados

app = FastAPI(title="Helpdesk API Modular")

# Conectando as peças
app.include_router(analistas.router)
app.include_router(chamados.router)
