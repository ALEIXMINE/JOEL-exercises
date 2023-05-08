# Nom: Sumar MÉS Digits
# Enllaç: https://jo-el.es/problem/sumardigits2

for i in range(int(input())):
    value = int(input())
    while len(str(value))!=1:
        total=0
        for n in list(str(value)):total+=int(n)
        value=total
    if len(str(value))==1:print(value)