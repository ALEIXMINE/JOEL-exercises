# Nom: Podriamos Tener Punto G
# Enllaç: https://jo-el.es/problem/podriamospuntog

llista=[]
for i in range(5):llista.append(input())
count=llista.count("G")
if count==1:print("SI")
elif count>1:print("PUNTOS")
else:print("NO")