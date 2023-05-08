# Nom: De Dia a Mes
# Enllaç: https://jo-el.es/problem/dediaames

dies_mesos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia = int(input())
mes = 1
while dia > dies_mesos[mes - 1]:
    dia -= dies_mesos[mes - 1]
    mes += 1
print(mes)