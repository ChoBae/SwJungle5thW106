# 재귀함수 카드놓기 5568
from itertools import permutations
import sys
n = int(input())
k = int(input())

a = [input() for _ in range(n)]
resert = set()
for i in permutations(a, k):
    resert.add(''.join(i))
# card_list = list(permutations(a, k))
# resert = set(card_list)
print(len(resert))