# Nom: Black Friday
# Enllaç: https://jo-el.es/problem/blackfriday

a=input().split(" ")
lines, cols = int(a[0]),int(a[1])
lines=[input().split(" ") for i in range(cols)]
mul=int(input())
matriz = [[int(l)*mul for l in lines[s[0]]] for s in enumerate(lines)]
c=0
data=""
def impri(t):
  global c, data, r
  c+=1
  if c==3:
    data+=str(t)
    print(data)
    data=""
    c=0
    return
  data+=str(t)+" "
[[[impri(i)] for i in l] for l in matriz]