# Nom: Eleccions 2020 (3)
# Enllaç: https://jo-el.es/problem/eleccions20203

vots=[]
for i in range(3):vots.append(int(input()))
if vots[0]>vots[1] and vots[0]>vots[2]: print("Jiden")
elif vots[1]>vots[0] and vots[1]>vots[2]: print("Drump")
else:print("Banders")