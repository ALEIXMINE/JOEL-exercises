# Nom: Pedra Paper Tisores
# Enllaç: https://jo-el.es/problem/pedrapaper

jugadors,valid = [int(input()) for i in range(2)],[1,2,3]
if jugadors[0] not in valid or jugadors[1] not in valid:
    print("ERROR")
else:
    if jugadors[0]==jugadors[1]:print("EMPAT")

    if jugadors[0]==1 and jugadors[1]==2:print("Jugador2")
    if jugadors[0]==1 and jugadors[1]==3:print("Jugador1")

    if jugadors[0]==2 and jugadors[1]==1:print("Jugador1")
    if jugadors[0]==2 and jugadors[1]==3:print("Jugador2")

    if jugadors[0]==3 and jugadors[1]==1:print("Jugador2")
    if jugadors[0]==3 and jugadors[1]==2:print("Jugador1")