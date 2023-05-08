# Nom: Fer la 13-14
# Enllaç: https://jo-el.es/problem/ferla1314

for i in range(int(input())):
    medides = input().split("-")
    if int(medides[0])<int(medides[1]) and int(medides[1])-int(medides[0])==1:
        if int(medides[0]) & 1 == 0:
            print("SI")
            continue
    print("NO")