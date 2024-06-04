import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Ex 1
"""with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)"""


# EX 2

try:
    with open(ROOT_PATH / "users.csv", "w", encoding="utf-8", newline="") as file:
        escritor = csv.writer(file)
        escritor.writerow(["id", "nome", "idade"])
        escritor.writerow(["1", "Maria", 25])
        escritor.writerow(["2", "João", 35])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "users.csv", "r", encoding="utf/8") as file:
        leitor = csv.reader(file)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "users.csv", "r", encoding="utf/8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
