# Nom: Números romans
# Enllaç: https://jo-el.es/problem/numerosromans

def convertir_a_romans(n):
    valors = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    romans = ''
    for i in range(len(valors)):
        while n >= valors[i]:
            romans += simbols[i]
            n -= valors[i]
    return romans

num_cases = int(input())
for i in range(num_cases):
    n = int(input())
    print(convertir_a_romans(n))