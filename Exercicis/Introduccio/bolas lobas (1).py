# Nom: bolas lobas (1)
# Enllaç: https://jo-el.es/problem/bolaslobas

for i in range(int(input())):
  word,chars=input(),input().split(" ")
  letters=[word[int(chars[0])],word[int(chars[1])]]
  print(word[:int(chars[0])]+letters[1]+word[int(chars[0])+1:int(chars[1])]+letters[0]+word[int(chars[1])+1:])