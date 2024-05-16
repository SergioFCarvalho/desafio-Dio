"""São tipos especiais de iteradores, não armazenam todos os seu valores na memória.
São definidos usando funções regulares, mas, ao invés de retornar valores usando (return), utilizam yield"""


def my_generator(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in my_generator(numeros=[10, 25, 35]):
    print(i)
