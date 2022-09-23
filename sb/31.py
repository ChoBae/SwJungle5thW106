# 2750 수 정렬하기
import sys
input = sys.stdin.readline
n = int(input())    # n개의 숫자
NumList = []    # 숫자리스트
for _ in range(n):  # n개의 숫자 숫자리스트에 넣어주기
    NumList.append(int(input()))
NumList.sort()  # 숫자리스트 오름차순으로 정렬
# 출력
for n in NumList:
    print(n)