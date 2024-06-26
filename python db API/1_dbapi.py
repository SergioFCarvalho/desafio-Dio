# Explorando Banco de Dados Relacionais com Python DB API
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# Criando conexão com BD
con = sqlite3.connect(ROOT_PATH / 'my_bank.db')
cursor = con.cursor()
cursor.row_factory = sqlite3.Row

# Criando uma tabela


def criar_tabela(con, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    con.commit()


# Inserindo dados na tabela
# inserir_dados(con, cursor, 'Saulo', 'saulo@gmail.com')
def inserir_dados(con, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);", (data))
    con.commit()


# Atualiza dado na tabela
# atualizar_dados(con, cursor, 'Ruth', 'ruth@hotmail.com', 2)
def atualizar_dados(con, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    con.commit()


# Exclui/ remover dado na tabela
# excluir_dados(con, cursor, 1)
def excluir_dados(con, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    con.commit()


# Inserindo dados em lote
# inserindo_muitos(con, cursor, dados)

def inserindo_muitos(con, curso, dados):
    curso.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    con.commit()


dados = [
    ('Maria', 'maria@example.com'),
    ('Carlos', 'carlos@example.com'),
    ('Ana', 'ana@example.com'),
    ('Mary', 'maryjane@example.com')
]
# Consultando 1 dado da tabela


def consultar_dado(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_dados(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY email;")


clientes = listar_dados(cursor)
for cliente in clientes:
    print(dict(cliente))

# row_factory personalize a forma como os resultados das consultas SQL são retornados {dict}


def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


cliente = recuperar_cliente(cursor, 5)
# print(dict(cliente))
