# Nom: de Segons a Hora
# Enllaç: https://jo-el.es/problem/segonsahora

hora = [0,0,int(input())]
res, surplus = divmod(hora[2], 60)
if res>0:hora[1]=res
hora[2]=surplus
res, surplus = divmod(hora[1], 60)
if res>0:hora[0]=res
hora[1]=surplus
print(":".join(map(str,hora)))