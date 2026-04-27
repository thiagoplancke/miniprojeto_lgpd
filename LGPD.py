from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert, text
from datetime import datetime
import csv
import os


import time
from functools import wraps
def medir_tempo(func):
    """Decorator que mede o tempo de execução de uma função."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # tempo inicial (mais preciso que time.time)
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()     # tempo final
        duracao = fim - inicio
        print(f"⏱ Função '{func.__name__}' executada em {duracao:.6f} segundos.")
        return resultado
    return wrapper

engine = create_engine("postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2", echo=False)
metadata = MetaData()

usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

metadata.create_all(engine)



def anonimizar_nome(nome):
    nome_ = nome.split()
    nome_[0] = nome_[0].replace(nome_[0][1:len(nome_[0])],"*"*(len(nome_[0])-1))
    nome_ = " ".join(nome_)

    return nome_
def anonimizar_cpf(cpf):
    cpf_ = ""
    for indice, j in enumerate(cpf):
        if indice >= 4 and indice <= 6:
            j = "*"
        if indice >= 8 and indice <= 10:
            j = "*"
        if indice >= 12 and indice <= 13:
            j = "*"
        cpf_= cpf_ + j

    

    return cpf_


def anonimizar_email(email):

        usuario, dominio = email.split("@")
        
        usuario_anon = usuario[0] + "*" * (len(usuario) - 1)
    
        return usuario_anon + "@" + dominio

def anonimizar_telefone(telefone):

    telefone_ = telefone[(len(telefone)-4):len(telefone)]
    return telefone_  
@medir_tempo
def criar_arquivo_csv_por_ano(user):
    data_ = str(user["data_nascimento"])
    filename = f'usuarios{data_[:4]}.csv'
    file_exist = os.path.isfile(filename)

    dados = [["id","Nome","CPF","Email","Telefone","Data de Nascimento"],
             [str(user["id"]),str(user["nome"]),str(user["cpf"]),str(user["email"]),str(user["telefone"]),str(user["data_nascimento"])]]

    if not file_exist:
        with open(filename, 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(dados)
    else:
        with open(filename, 'a', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(dados[1])

@medir_tempo
def criar_todos(user):
    filename = f'todos.csv'
    file_exist = os.path.isfile(filename)

    dados = [["Nome","CPF"],
             [str(user["nome"]),str(user["cpf"])]]
    if not file_exist:
        with open(filename, 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(dados)
    else:
        with open(filename, 'a', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(dados[1])


@medir_tempo
def LGPD(row):
    base_original = {"id": row.id,
            "nome":row.nome,
            "cpf": row.cpf,
            "email": row.email,
            "telefone":row.telefone,
            "data_nascimento": row.data_nascimento}
    base_anonimizada = base_original.copy()
    base_anonimizada["nome"] = anonimizar_nome(row.nome)
    base_anonimizada["cpf"] = anonimizar_cpf(row.cpf)
    base_anonimizada["email"] = anonimizar_email(row.email)
    base_anonimizada["telefone"] = anonimizar_telefone(row.telefone)
    return base_anonimizada, base_original

users = []
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 10;"))
    for row in result:
        row,org = LGPD(row)
        users.append((row,org))
        

for user in users:
    print(user[0])
    medir_tempo(criar_arquivo_csv_por_ano(user[0]))
    medir_tempo(criar_todos(user[1]))











