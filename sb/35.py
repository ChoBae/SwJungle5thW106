# 2309 일곱난쟁이
# 풀이 1
from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]   # 9난쟁이 리스트
Comb = list(combinations(dwarfs, 7))    # 9명의 난쟁이의 조합(7명) 구하기
# 조합별로 탐색
for com in Comb:
    # 해당 조합의 키의 합이 100이면 정답
    if sum(com) == 100:
        res = list(com)  # com이 튜플형식이기에 정렬을 위한 변환
        res.sort()  # 오름차순 정렬
        for r in res:   # 출력
            print(r)
        break


# 풀이2
# # 아홉난쟁이 키 리스트
# ninedwarf = [int(input()) for i in range(9)]
# # 아홉난쟁이의 키를 더한 값
# ninedwarfSum = sum(ninedwarf)
# # 아홉 난쟁이 반복
# for i in range(9):
#     # 0,1-> 0,2 ..... 1,2 -> 1,3 ... 비교
#     for j in range(i+1, 9):
#         # 두 명의 난쟁이를 아홉난쟁이의 키에서 뺐을때 100이 된다면 값을 리스트에 제거해주고 반복문 break
#         if ninedwarfSum - ninedwarf[i] - ninedwarf[j] == 100:
#             deleteDwarf1 = ninedwarf[i]
#             deleteDwarf2 = ninedwarf[j]
#             ninedwarf.remove(deleteDwarf1)
#             ninedwarf.remove(deleteDwarf2)
#             ninedwarf.sort()
#             break
#     # 이미 결과값이 나왔을때 반복문 break
#     if len(ninedwarf) < 9:
#         break
# # 출력
# for dwarf in ninedwarf:
#     print(dwarf)
