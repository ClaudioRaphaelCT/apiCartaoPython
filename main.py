from fastapi import FastAPI
from model.CartaoModel import ItemCreate
from controller.methods import Metodos

app = FastAPI()

# Criar a tabela se não existir
Metodos.create_table()

@app.get("/uso")
def obter():
   return Metodos.get()

@app.post("/inserir")
def setItem(item: ItemCreate):
   return Metodos.insert(item)

@app.get('/quantidade')
def obter_quantidade():
   return Metodos.count()

