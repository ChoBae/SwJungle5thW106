# X보다 작은 수
n, x = map(int, input().split())
NumList = list(map(int, input().split()))
for i in range(n):
    if NumList[i] < x:
        print(NumList[i], end=' ')
