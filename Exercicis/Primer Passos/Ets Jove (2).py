# Nom: Ets Jove (2)
# Enllaç: https://jo-el.es/problem/etsjove2

c=0
numbers=input().split(" ")
for i in numbers:
    if int(i)<31:c+=1
print(c)