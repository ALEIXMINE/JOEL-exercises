# Nom: Caga tió!
# Enllaç: https://jo-el.es/problem/cagatio

for i in range(int(input())):
    gen = int(input())
    cops=0
    while gen>2:
        cops+=1
        gen-=2
    print(f"Caga","caga"*cops+"tio!")