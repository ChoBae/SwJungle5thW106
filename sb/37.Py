# 10819 차이를 최대로
from itertools import permutations
import sys
input = sys.stdin.readline
# 1번 풀이 -> permutation(순열) 풀이
n = int(input())    # n개의 수로 이루어진  배열 a
a = list(map(int, input().split()))
per = permutations(a)   # a리스트 순열 변환
res = 0 # 결과값 설정
# 순열 탐색
for p in per:
    tmp = 0 # 현재 조건 값
    for i in range(len(p)-1):
        tmp += abs(p[i] - p[i+1])   # 현재 조건값 구하기
    # 탐색을 마치고, 현재 저장된 결과값이랑 비교함
    if res < tmp:
        res = tmp
# 출력
print(res)