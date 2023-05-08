# Nom: Quadra't
# Enllaç: https://jo-el.es/problem/cuadrate

for i in range(int(input())):
    n, m = map(int, input().split())
    total_quadrats = 0
    for j in range(1, min(n, m)+1):
        total_quadrats += (n-j+1)*(m-j+1)
    print(total_quadrats)