# Nom: Te'n recordes de...
# Enllaç: https://jo-el.es/problem/recordesde

for i in range(int(input())):
    k,nums,p = int(input()),list(map(int, input().split())),int(input())
    print(sorted(nums)[p])