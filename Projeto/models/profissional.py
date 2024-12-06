# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from models.modelopersistencia import CRUD

# Modelo
class Profissional:
  def __init__(self, id, nome, especialidade, conselho):
    self.id = id
    self.nome = nome
    self.especialidade = especialidade
    self.conselho = conselho
  def __str__(self):
    return f"{self.nome} - {self.especialidade} - {self.conselho}"

# Persistência
class Profissionais(CRUD):

  @classmethod
  def salvar(cls):
    with open("profissionais.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("profissionais.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Profissional(obj["id"], obj["nome"], obj["especialidade"], obj["conselho"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

