# 정렬 수 정렬하기2
import sys


input = sys.stdin.readline
n = int(input())

a = [int(input()) for _ in range(n)]
# a.sort()
b = sorted(a)
for i in range(n):
    print(b[i])