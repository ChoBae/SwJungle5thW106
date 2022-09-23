# 1978 소수찾기
# 소수 체크 함수 -> 에라토스테네스의 체가 제일 속도가 빨랐던것같음
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())
NumList = list(map(int, input().split()))
res = 0
for n in NumList:
    if prime(n) and n > 1:
        res += 1

print(res)
