# Lidando com Data, Hora e Fuso Horário no Python

# Formatando e convertendo datas com strftime e strptime

# EX 1
import pytz
import datetime

data_hora_atual = datetime.datetime.now()
date_string = "20/05/2024 15:30"
mascara_ptbr = "%d/%m/%Y %H:%M"

# Formatando data e hora
print(data_hora_atual.strftime(mascara_ptbr))

# Convertendo string para datetime

d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)

# Trabalhando com timezone

# EX

# Criando datetime com timezone
dat = datetime.datetime.now(pytz.timezone("America/Sao_paulo"))
