from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Exemplo de código

with open(ROOT_PATH / 'example.txt', 'r') as file:
    print("Trabalhando com arquivo")
    print(file.read())


# enconding = utf-8 / enconding = ascii
try:
    with open(ROOT_PATH / 'example.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write("aprendendo py")
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
