# Nom: Llibres a la prestatgeria
# Enllaç: https://jo-el.es/problem/llibresquenohicaben

N,M,K = [int(input()) for i in range(3)]
R=K-N*M
print(0 if R<0 else R)