# 14888 연산자 끼워넣기
from itertools import permutations
import sys

# 1번 순열풀이 -> pypy3 통과(DFS 써서 풀어보자)
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


# 2번 DFS풀이 -> py
# 백트래킹 (Python3 통과, PyPy3도 통과)
# import sys

# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # +, -, *, //

# maximum = -1e9
# minimum = 1e9

# # dfs
# def dfs(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum # 전역변수 선언
#     # 깊이가 N일때 최대, 최소값 업데이트 후 리턴
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return
#     # 모든 경우의 수 탐색
#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]),
#             plus, minus, multiply, divide - 1)

# dfs(1, num[0], op[0], op[1], op[2], op[3])  # dfs 진행
# # 출력
# print(maximum)
# print(minimum)

# 3번 Dfs 끄적
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
cal = list(map(int, input().split()))
MaxNum = -10e9
MinNum = 10e9


def dfs(depth, sum, plus, minus, mul, div):
    global MaxNum, MinNum
    if depth == n:
        MaxNum = max(MaxNum, sum)
        MinNum = min(MinNum, sum)

    if plus:
        dfs(depth+1, sum + a[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, sum-a[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, sum * a[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth+1, int(sum/a[depth]), plus, minus, mul, div-1)


dfs(1, a[0], cal[0], cal[1], cal[2], cal
    [3])
print(MaxNum)
print(MinNum)