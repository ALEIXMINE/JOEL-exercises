# Nom: Cercar Trios
# Enllaç: https://jo-el.es/problem/buscartrios

ls1 = [int(input()),int(input()),int(input())]
print("SI" if all([val == ls1[0] for val in ls1]) else "NO")