# Nom: Primers
# Enllaç: https://jo-el.es/problem/primers

from math import *
def is_prime(number):
    if number <= 1:return False
    if number == 2:return True
    if number % 2 == 0:return False
    limit = floor(sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:return False
    return True

while True:
  i=int(input())
  if i==-1:break
  print("SI" if is_prime(i) else "NO")