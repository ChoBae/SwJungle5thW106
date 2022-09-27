# 14888 연산자 끼워넣기
from itertools import permutations
import sys

## 1번 순열풀이 -> pypy3 통과(DFS 써서 풀어보자)
# input = sys.stdin.readline
# n = int(input())
# a = list(map(int, input().split()))
# cal = list(map(int, input().split()))  # +, - , *, / 의 수
# calLi = ["+", "-", "*", "/"]
# rr = ''
# for i in range(len(cal)):
#     rr += cal[i] * calLi[i]
# per = list(permutations(rr))
# MaxRes = -10e9
# MinRes = 10e9
# for p in per:
#     tmp = a[0]
#     for i in range(len(p)):
#         if p[i] == '+':
#             tmp += a[i+1]
#         elif p[i] == '-':
#             tmp -= a[i+1]
#         elif p[i] == '*':
#             tmp *= a[i+1]
#         else:
#             tmp /= a[i+1]
#             tmp = int(tmp)

#     MaxRes = max(MaxRes, tmp)
#     MinRes = min(MinRes, tmp)


# print(MaxRes)
# print(MinRes)


## 2번 DFS풀이 -> py
