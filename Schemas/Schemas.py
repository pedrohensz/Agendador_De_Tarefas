from pydantic import BaseModel
from datetime import time
from typing import List, Optional

class TarefaCreate(BaseModel):
    nome:str  
    descricao:str = ""
    concluida:bool = False
    horario:time

    class Config:
        from_attributes = True

class TarefaResponse(BaseModel):
    id: int
    nome:str  
    descricao:str
    concluida:bool
    horario:time
