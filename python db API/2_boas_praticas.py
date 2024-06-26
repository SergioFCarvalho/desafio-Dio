# Explorando Banco de Dados Relacionais com Python DB API
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# Criando conexão com BD
con = sqlite3.connect(ROOT_PATH / 'my_bank.db')
cursor = con.cursor()
cursor.row_factory = sqlite3.Row


# Evite isso
id = 1
cursor.execute('SELECT * FROM clientes WHERE id = ' + str(id))

# Faça isto
id = 1
cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
