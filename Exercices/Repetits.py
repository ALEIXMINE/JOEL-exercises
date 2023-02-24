# Nom: Repetits
# Enllaç: https://jo-el.es/problem/repetits

for i in range(int(input())):
    numeros=int(input())
    llista_de_numeros=list(map(int, input().split()))
    repetit=False
    for i in range(numeros):
        for j in range(i + 1, numeros):
            if llista_de_numeros[i] == llista_de_numeros[j]:
                repetit=True
                break
    print("SI" if repetit else "NO")