# Nom: Qui és més vell?
# Enllaç: https://jo-el.es/problem/mesvell

nom1, edat1, nom2, edat2= input(), int(input()), input(), int(input())
if edat1<edat2:print(nom2)
elif edat1>edat2:print(nom1)
else:print("Cap és més vell")