# -- Lidando com Data, Hora e Fuso Horário no Python
# Trabalhando com objetos date, datetime e time
from datetime import date, datetime, time, timedelta
# - Date -
data = date(2024, 5, 18)
print(data)
data_atual = date.today()
print(data_atual)
# - Datetime -
data_hora = datetime(2024, 5, 20, 15, 30, 45)
print(data_hora)
data_hora_atual = datetime.today()
print(data_hora_atual)
# - Time -
hora = time(17, 16, 30)
print(hora)

# > Manipulando datas com timedelta
# - Criando data e hora
d = datetime(2024, 5, 18, 20, 15, 45)
print(d)  # 2024-05-18:20:15
# - Adicionando uma semana
d = d + timedelta(weeks=1)
print(d)  # 2024-05-25 20:15:45

# EX2
tipo_carro = "P"  # P, M, G
tempo_p = 30
tempo_m = 45
tempo_g = 60
data_de_hoje = datetime.now()

if tipo_carro == "P":
    data_estimada = data_de_hoje + timedelta(minutes=tempo_p)
    print(f"O carro chegou: {data_de_hoje} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_de_hoje + timedelta(minutes=tempo_m)
    print(f"O carro chegou: {data_de_hoje} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_de_hoje + timedelta(minutes=tempo_g)
    print(f"O carro chegou: {data_de_hoje} e ficará pronto às {data_estimada}")

# EX3
# Horário de entrada
hora_entrada = datetime(2024, 5, 18, 8, 0, 0)

# Horário de saída
hora_saida = datetime(2024, 5, 18, 17, 0, 0)

# Cálculo da duração da jornada
tempo_trabalho = hora_saida - hora_entrada

print(f"Tempo de trabalho: {tempo_trabalho}")

# EX4
resultado = datetime(2024, 5, 18, 18, 40, 45) + timedelta(hours=1)
print(f"Capturando apenas o tempo: \033[1;41m{resultado.time()}\033[m")
print(f"Capturando apenas a data: \033[1;42m{datetime.now().date()}\033[m")
