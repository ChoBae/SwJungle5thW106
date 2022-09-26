# 정렬, 수정렬하기
n = int(input())

a = [int(input()) for _ in range(n)]
a_sort = sorted(a)

for i in range(n):
    print(a_sort[i])