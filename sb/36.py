# 2798 블랙잭
from itertools import combinations
n, m = map(int, input().split())    # n(카드 갯수), m(타겟 숫자)
CardLi = list(map(int, input().split()))    # 카드리스트
Comb = list(combinations(CardLi, 3))    # 카드리스트의 조합
res = -10e9 # 결과값 초기설정 -> 가장큰수!
for com in Comb:    # 조합별 완전탐색
    PreSum = sum(com)
    # 카드 3장의 합이 M(타겟숫자) 이하 이고, 현재의 결과값보다 클때
    if PreSum <= m and res < PreSum:
        res = PreSum    # 결과값 업데이트
        # 결과값이 타겟값과 같다면 탐색 중단
        if res == m:
            break
# 출력
print(res)
        