# Nom: Jordi while() 2
# Enllaç: https://jo-el.es/problem/jordiwhile2

numbers = input().split()
total=0
for i in numbers:
  if int(i)==-1:continue
  total+=int(i)
print(total)