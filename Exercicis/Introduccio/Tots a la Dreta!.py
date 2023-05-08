# Nom: Tots a la Dreta!
# Enllaç: https://jo-el.es/problem/totsaladreta

N=int(input())
lista=input().split(" ")
lista=[lista[N-1]]+lista[0:N-1]
print(" ".join(lista))