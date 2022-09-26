# 재귀함수 팩토리얼 10872
n = int(input())

a = 1
for i in range(2 , n+1):
    a = a*i
print(a)