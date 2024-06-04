# Exemplo de código

"""# Para ler um arquivo
file = open('example.txt', 'r')
# Para escrever em um arquivo
file = open('example.txt', 'w')
# Para anexar conteúdo a um arquivo existente
file = open('example.txt', 'a')"""

""" 
Python fornece várias maneiras de ler um arquivo. Podemos usar 'read()', 'readline()' ou 'readlines()' dependendo de nossas necessidades 
"""
# Método readlines:
"""file = open('manipulando_arq/example.txt', 'r')
print(file.read())
print(file.readline())
print(file.readlines())
while len(linha := file.readline()):
    print(linha)
file.close()"""


txt = "Podemos usar 'write()' ou 'writelines' para escrever em um arquivo. Lembre-se de abrir o arquivo no modo correto."

# Exemplo
file = open('manipulando_arq/teste.txt', 'w')
file.write(txt)
file.writelines(["\n", "Hello ", "programmer "])
file.close()
