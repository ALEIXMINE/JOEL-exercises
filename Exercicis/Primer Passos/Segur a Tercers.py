# Nom: Segur a Tercers
# Enllaç: https://jo-el.es/problem/seguroaterceros

pared,alumne,patinet=float(input()),float(input()),float(input())
if abs(pared-alumne)<=patinet:print("SEGURO")
else:print("OK")