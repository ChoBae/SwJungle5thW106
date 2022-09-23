# 10989 수 정렬하기 3
import sys
input = sys.stdin.readline
n = int(input())    # 입력 (n개의 수)
NumIndex = [0] * 10001  # 최대 숫자 크기인 10000까지 인덱싱 처리
for _ in range(n):  # 숫자에 해당하는 인덱스에 갯수 추가
    NumIndex[int(input())] += 1
# 10000까지 반복
for i in range(10001):
    if NumIndex[i] != 0:  # i인덱스가 0이 아니라면 존재하는 수 -> 존재하는 만큼 출력해줌
        for j in range(NumIndex[i]):
            print(i)
