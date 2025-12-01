from fastapi import FastAPI, Depends, HTTPException
from Schemas.Schemas import TarefaCreate, TarefaResponse
from Services.Services import Tarefas
from Database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from Models.Objects import Tarefa
from sqlalchemy.orm import joinedload
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()
service = Tarefas()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://127.0.0.1:5500"] se estiver usando Live Server
    allow_methods=["*"],  # permite GET, POST, PUT, DELETE
    allow_headers=["*"],)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/tarefas", response_model= TarefaCreate)
def criar_tarefa(tarefa: TarefaCreate,
                 db:Session = Depends(get_db)
                 ):
    db_tarefa = Tarefa(
    nome=tarefa.nome,
    descricao=tarefa.descricao,
    horario=tarefa.horario,
    concluida=tarefa.concluida
)
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

@app.get("/tarefas", response_model=list[TarefaResponse])
def ler_tarefas(db: Session = Depends(get_db)):
    tarefas = db.query(Tarefa).all()
    return tarefas

@app.put("/tarefas/{id}")
def atualizar_tarefa(id:int,db:Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    else:
        if tarefa.concluida == True:
            tarefa.concluida = False
            db.commit()
            return {"Mensagem": "Tarefa desmarcada como concluída."}
        else:
            tarefa.concluida = True
        db.commit()
        return {"Mensagem": "Tarefa concluída com sucesso."}



@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int, db: Session = Depends(get_db)):

    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db.delete(tarefa)
    db.commit()

    return {"Mensagem": "Tarefa deletada com sucesso."}