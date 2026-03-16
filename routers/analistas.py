from fastapi import APIRouter

router = APIRouter(prefix="/analistas", tags=["Equipe de TI"])

@router.get("/")
def listar_analistas():
    return [{"id": 1, "nome": "Sidney"}, {"id": 2, "nome": "Mariana"}]

@router.post("/")
def criar_analista():
    return {"msg": "Analista criado com sucesso"}

