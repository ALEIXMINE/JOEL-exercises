# Nom: Bucles 1 - Valor més gran i més petit
# Enllaç: https://jo-el.es/problem/mesgranpetit

llista=[]
while True:
    nb=int(input())
    if nb==0:break
    llista.append(nb)
print(max(llista),min(llista))