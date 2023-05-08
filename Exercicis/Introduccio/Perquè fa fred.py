# Nom: Perquè fa fred
# Enllaç: https://jo-el.es/problem/fafred

fred=[]
for i in input().split(" "):
  if int(i)<0:fred.append(int(i))
print(len(fred))
print(sum(fred)/len(fred))