from fastapi import APIRouter

router = APIRouter(prefix="/chamados", tags=["Atendimento"])

@router.get("/chamados")
def listar_chamados():
    return [
        {"id": 101, "problema": "Sem acesso à VPN", "status": "Aberto"},
        {"id": 102, "problema": "Troca de teclado", "status": "Fechado"}
    ]

@router.post("/chamados")
def abrir_chamado():
    return {"msg": "Chamado registrado no sistema"}

    