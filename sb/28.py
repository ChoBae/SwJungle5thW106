# 1914 하노이의 탑
# 첫 풀이 -> 시간초과.
# def hanoi(n, x, y):
#     global move, check, res
#     if n > 1:
#         hanoi(n-1, x, 6-x-y)

#     if check:
#         move.append((x, y))
#     res += 1

#     if n > 1:
#         hanoi(n-1, 6-x-y, y)


# n = int(input())  # 원판의 갯수
# check = True
# if n > 20:
#     check = False
# move = []
# res = 0
# hanoi(n, 1, 3)

# print(len(move))
# if move:
#     for x, y in move:
#         print(x, y)


# 두번쨰 풀이 -> 재귀 중간중간 연산을 빼고 원판 이동횟수의 총합은 따로 구한다.
# hanoi(n번째 원판, x번째 장대, y번쨰 장대 )
def hanoi(n, x, y):
    if n > 1:
        hanoi(n-1, x, 6-x-y)
    # 이동 상황 출력
    print(x, y)

    if n > 1:
        hanoi(n-1, 6-x-y, y)


n = int(input())  # 원판의 갯수
print(2**n - 1) # 이동횟수의 총합
if n <= 20: # n이 20이하일때 이동 상황까지 출력
    hanoi(n, 1, 3)
