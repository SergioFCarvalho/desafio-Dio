# Solicita ao usuário que insira o consumo médio mensal de dados:
print("Qual consumo?")
consumo = float(input())
print(consumo)
# Construção da função


def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo >= 20:
        return "Plano Premium Fibra - 300Mbps"


# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
