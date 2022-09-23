# 9020 골드바흐의 추측
from itertools import combinations, combinations_with_replacement

# 첫풀이 -> 실패
# 1. 인풋값을 모두 모아서 가장 큰 수를 기준으로 소수리스트 구하기
# 2. 테스트케이스들을 각각의 소수리스트를 중복 조합을 구해서 정답 유추 -> 시간초과
# # 소수 체크 함수 -> 에라토스테네스의 체
# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n

#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우
#             for j in range(i+i, n, i):  # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]
# # 중복조합 함수
# def Combi(li, n):
#     # n까지의 소수리스트에서 중복조합 찾기
#     CombLi = list(combinations_with_replacement(li, 2))
#     minNum = 10e9   # 만족하는 조건의 두수의 차이 중 최소값
#     res = ''    # 결과값
#     # 중복 조합 내에서 정답 찾기
#     for com in CombLi:
#         # 해당 조합의 합이 주어진 수 n이라면
#         if sum(com) == n:
#             # 최솟값 인지 확인하기
#             if minNum > abs(com[0]-com[1]):
#                 minNum = abs(com[0]-com[1])
#                 res = str(com[0]) + ' ' + str(com[1])
#     # 정답출력
#     return res


# t = int(input())    # 테스트 케이스의 수
# TestCase = []# 테스트 케이스
# for _ in range(t):
#     n = int(input())    # 주어진 수 n
#     TestCase.append(n)

# PrimeList = prime_list(max(TestCase))
# for num in TestCase:
#     nowPrimeList = []
#     for n in PrimeList:
#         if n < num:
#             nowPrimeList.append(n)

#     print(Combi(nowPrimeList, num))
##  풀이 2 -> 성공
# 1. 두 변수를 통해 하나는 +1, 하나는 -1 하며 두수가 소수가 됐을때를 확인해서 정답을 유추함
# 소수 체크 함수
def primeCheck(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


t = int(input())    # 테스트 케이스
for _ in range(t):  # 테스트 케이스 확인
    n = int(input())    # 주어진 n
    UpNum, DownNum = n // 2, n // 2 # n을 2등분해서 동일하게 올라갈 변수와 내려갈 변수를 만듦
    while True:
        # +1 한 수와 -1 한 수가 모두 소수 일때 출력
        if primeCheck(UpNum) and primeCheck(DownNum):
            print(DownNum,UpNum)
            break
        else:
            UpNum += 1
            DownNum -= 1
