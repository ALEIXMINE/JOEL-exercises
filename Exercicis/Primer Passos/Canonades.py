# Nom: Canonades
# Enllaç: https://jo-el.es/problem/canonades

meters = float(input())
if meters <= 25:total = meters * 3
elif meters <= 75:total = 25 * 3 + (meters - 25) * 4
else:total = 25 * 3 + 50 * 4 + (meters - 75) * 5
print(str(float(meters)) + "m: " + str(float(total)) + " euros")