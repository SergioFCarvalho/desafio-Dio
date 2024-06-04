import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criar um diretório
os.mkdir(ROOT_PATH / "new")

#  Cria um novo arquivo
file = open(ROOT_PATH / "newarq.txt", "w")
file.close()

# Renomear arquivo
os.rename(ROOT_PATH / "newarq.txt", ROOT_PATH / "new2.txt")


# # Remover arquivo
os.remove(ROOT_PATH / "new2.txt")

# Mover arquivo
shutil.move(ROOT_PATH / "newarq.txt", ROOT_PATH / "new" / "newarq.txt")
