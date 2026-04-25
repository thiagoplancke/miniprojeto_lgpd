from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert, text
from datetime import datetime

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



@medir_tempo
def LGPD(row):
    base_original = {"id": row.id,
            "nome":row.nome,
            "cpf": row.cpf,
            "email": row.email,
            "telefone":row.telefone,
            "data_nascimento": row.data_nascimento}
    base_anonimizada = base_original
    base_anonimizada["nome"] = anonimizar_nome(row.nome)
    return base_anonimizada

users = []
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 5;"))
    for row in result:
        row = LGPD(row)
        users.append(row)
        

for user in users:
    print(user)
