# Nom: El cistell de la compra
# Enllaç: https://jo-el.es/problem/cistellcompra

elements = []
for i in range(int(input())):
  e = input().split(" ")
  elements.append([e[0],float(e[1])])
search=int(input())-1
def sortSecond(val):return val[1]
elements.sort(key=sortSecond,reverse=True)
print("EL MES CAR:",elements[0][0],elements[0][1])
print("EL MES BARAT:",elements[len(elements)-1][0],elements[len(elements)-1][1])
print("EL BUSCAT:",elements[search][0],elements[search][1])