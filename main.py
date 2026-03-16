from fastapi import FastAPI

app = FastAPI(title="Helpdesk API Monolítica")

@app.get("/analistas")
def listar_analistas():
    return [{"id": 1, "nome": "Sidney"}, {"id": 2, "nome": "Mariana"}]

@app.post("/analistas")
def criar_analista():
    return {"msg": "Analista criado com sucesso"}

@app.get("/chamados")
def listar_chamados():
    return [
        {"id": 101, "problema": "Sem acesso à VPN", "status": "Aberto"},
        {"id": 102, "problema": "Troca de teclado", "status": "Fechado"}
    ]

@app.post("/chamados")
def abrir_chamado():
    return {"msg": "Chamado registrado no sistema"}

