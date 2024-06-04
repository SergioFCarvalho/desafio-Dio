# ❌FileNotFoundError
try:
    file = open("my_file.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)


# ❌IsADirectoryError
try:
    file = open("new")
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
