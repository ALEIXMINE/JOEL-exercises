# Nom: El Radar de la Valentina
# Enllaç: https://jo-el.es/problem/radarvalentina

for i in range(int(input())):
    energia=max(map(int,input().split()))
    if energia<1000:print("H")
    elif 10000>energia>=1000:print("B")
    else:print("M")