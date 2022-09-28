# 카드 놓기 5568
from itertools import permutations

## 풀이1 순열풀이
# 입력
n = int(input())
k = int(input())
CardList = []   # 카드리스트
# 카드리스트에 넣어주기
for _ in range(n):
    CardNum = int(input())
    CardList.append(CardNum)
# permutations함수(순열) 사용
PerLi = list(permutations(CardList, k))
res = []    # 답안
# 조합들 체크
for p in PerLi:
    tmp = ''    # 현재 조합의 정수형태
    # 하나씩 합치기
    for now in p:
        tmp += str(now)
    # 현재 조합된 형태가 없을때만 답안리스트에 넣어주기
    if tmp not in res:
        res.append(tmp)
# 출력
print(len(res))
    
    
