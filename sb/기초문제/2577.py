# 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
tmp = a * b * c
for i in range(9):
    print(str(tmp).count(str(i)))
