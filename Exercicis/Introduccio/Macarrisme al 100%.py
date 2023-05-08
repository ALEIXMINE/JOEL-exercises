# Nom: Macarrisme al 100%
# Enllaç: https://jo-el.es/problem/stringclub1

llargada=int(input())
llista=[str(float(e)*100)+"% " for e in input().split(" ")]
print("".join(llista))