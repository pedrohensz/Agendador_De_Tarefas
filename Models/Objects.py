from Database import Base
from sqlalchemy import Column, Integer, String, Boolean, Time

class Tarefa(Base):
    __tablename__ = "tarefas_prod"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    concluida = Column(Boolean, default=False)
    horario = Column(Time)

    def __str__(self):
        return f'{self.nome} | {self.descricao}'