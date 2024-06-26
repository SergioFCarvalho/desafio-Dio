import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# Criando conexão com BD
con = sqlite3.connect(ROOT_PATH / 'my_bank.db')
cursor = con.cursor()
cursor.row_factory = sqlite3.Row

"""O rollback() atua como uma rede de segurança, permitindo que você reverta todas as alterações feitas na transação caso algo dê errado."""

try:
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);", ('test1', 'test1@gmail.com'))
    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?);", (2, 'test1', 'test1@gmail.com'))
    con.commit()
except Exception as exc:
    print(f'Ops ocorreu um erro {exc}')
    con.rollback()
