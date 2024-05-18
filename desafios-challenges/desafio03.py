# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

import re


def validate_numero_telefone(phone_number):
    # Define o padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX
    pattern = r'\(\d{2}\) 9\d{4}-\d{4}'

    # Verifica se o padrão definido corresponde ao número de telefone fornecido
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input(
    "Digite um número de telefone no formato (XX) 9XXXX-XXXX: ")

# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento
result = validate_numero_telefone(phone_number)

# Imprime o resultado
print(result)
