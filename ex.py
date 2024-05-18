import time
# Exemplo de Estrutura de dados para um livro

livro = {
    'titulo': 'Dom Casmurro',
    'autor': 'Machado de Assis',
    'ano_publicacao': 1899,
    'genero': 'Romance'
}

# Exemplo de lista de livros

livros = [
    {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis',
        'ano_publicacao': 1899, 'genero': 'Romance'},
    {'titulo': '1984', 'autor': 'George Orwell',
        'ano_publicacao': 1949, 'genero': 'Ficção Científica'},
    {'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry',
        'ano_publicacao': 1943, 'genero': 'Infantil'},
    {'titulo': 'Poesia Que Transforma', 'autor': 'Bráulio Bessa',
        'ano_publicacao': 2018, 'genero': 'Poesia'}

]


def exibir_lista_de_livros(lista):
    print("\nLista de Livros:")
    print("----------------")
    for livro in lista:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de Publicação: {livro['ano_publicacao']}")
        print(f"Gênero: {livro['genero']}")
        print("----------------")


exibir_lista_de_livros(livros)
print('\n')


def remover_livro(lista):
    titulo_remover = input("Digite o título do livro que deseja remover: ")
    for livro in lista:
        if livro['titulo'] == titulo_remover:
            lista.remove(livro)
            print(f"O livro '{titulo_remover}' foi removido com sucesso!")
            return
    print(f"O livro '{titulo_remover}' não foi encontrado na lista.")


# Integrando as funções
remover_livro(livros)
time.sleep(2)
exibir_lista_de_livros(livros)
