# 정렬 수 정렬하기3 10989
import sys
input = sys.stdin.readline
n = int(input())

a = [0] * 10001
for _ in range(n):
    num = int(input())
    a[num] += 1
# 출력
for i in range(1,len(a)):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)