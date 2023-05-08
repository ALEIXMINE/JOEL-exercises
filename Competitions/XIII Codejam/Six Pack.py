# Nom: Six Pack
# Enllaç: https://jo-el.es/problem/sixpack

for _ in range(int(input())):
    cer,gim=0,0
    while True:
        e=input()
        if e=="BUFFFFF": break
        linestr = e.split(" ")
        for i in linestr:
            if i=="C":cer+=1
            if i=="G":gim+=1
    if cer>gim:print("Cervesa")
    elif gim>cer:print("Gimnas")
    else:print("Empat")
