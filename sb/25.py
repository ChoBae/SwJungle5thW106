# 10872 팩토리얼
# 반복문 풀이 -> 재귀도 비슷함!
# n = int(input())
# res = 1
# for i in range(1, n+1):
#     res *= i
# print(res)

# 재귀풀이
def fact(num):
    # 재귀는 정지 처리가 꼭 필요함.
    if num <= 1:
        return 1
    return num * fact(num-1)

n = int(input())
print(fact(n))