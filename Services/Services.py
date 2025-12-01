from Models.Objects import Tarefa

class Tarefas:
    def __init__(self):
        self.tarefas = []
        self.contador = 1

    def CriarTarefas(self,tarefas, nome, descricao, contador):
        tarefa = Tarefas(self.contador, nome, descricao)
        self.tarefas.append(tarefa)
        self.contador += 1
        return tarefa
    
    def ListarTarefas(self):
        return self.tarefa
    
    def DeletarTarefas(self, id):
        self.tarefas = [t for t in self.tarefas if t.id != id]