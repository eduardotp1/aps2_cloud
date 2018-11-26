import os
import requests
import json
import sys

#endereco="http://0.0.0.0:5000"
def adicionar(task):
    req = requests.post('http://localhost:5000/Tarefa', data=json.dumps({'task': task}))
    
def listar():
    req = requests.get('http://localhost:5000/Tarefa')

def buscar(id):
    req = requests.get('http://localhost:5000/Tarefa/'+id)

def apagar(id):
    req = requests.delete('http://localhost:5000/Tarefa/' +id)

def atualizar(id,task):
    req = requests.put('http://localhost:5000/Tarefa/' + id, data=json.dumps({'task': task}))

func=sys.argv[1]

if (func=="adicionar"):
    adicionar(sys.argv[2])
elif (func=="listar"):
    listar()
elif (func=="buscar"):
    buscar(sys.argv[2])
elif (func=="apagar"):
    apagar(sys.argv[2])
elif (func=="atualizar"):
    atualizar(sys.argv[2],sys.argv[3])
else:
    print("Corrija a funcao desejada")
