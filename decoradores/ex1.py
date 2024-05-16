def decorador1(funcao):
    def envelope():
        print('Faz algo antes de executar a função')
        funcao()
        print('Faz algo depois de executar a função')

    return envelope


"""O Python permite que usar decoradores de maneira mais simples com o símbolo @"""


@decorador1
def ola_mundo():
    print("Olá mundo ")


# ola_mundo = decorador1(ola_mundo) antes
ola_mundo()

print('\n')

""" > Funções de decoração com argumentos Usando *args e **kwargs na função interna, com isso aceitará um número de argumentos"""


def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return envelope


@duplicar
def aprender(tech):
    print(f"Estou aprendendo {tech}")
    return tech.upper()


tech = aprender("Python")
print(tech)
