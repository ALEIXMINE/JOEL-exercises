# Nom: Suma un Segon
# Enllaç: https://jo-el.es/problem/sumaunsegon

H,M,S=[int(input()) for i in range(3)]
EM,S=divmod(S+1,60)
EH,M=divmod(M+EM,60)
if H+EH>=24:H,EH=0,H+EH-24
print(H+EH,M,S)