# Nom: Jordi while()
# Enllaç: https://jo-el.es/problem/jordiwhile

il = input().split(" ")
videos=0
for i in il:
  if int(i)>0:videos+=1
print(videos)