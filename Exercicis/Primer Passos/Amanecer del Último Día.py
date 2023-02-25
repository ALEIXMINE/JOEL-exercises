# Nom: Amanecer del Último Día
# Enllaç: https://jo-el.es/problem/amanecerultimodia

segons = int(input())
durada_dia = 24 * 60 * 60
durada_periode = durada_dia // 2
dia = (segons // durada_dia) + 1
periode = (segons % durada_dia) // durada_periode
hora = "mati" if periode==0 else "nit"
print(hora + " del dia " + str(dia))