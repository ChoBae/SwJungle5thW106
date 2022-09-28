# 1074 Z
# z
# 1번 풀이 
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
visit = 0

while n != 0:
    print(n)
    n -= 1
    size = 2 ** n

    # 1사분면 처리
    if r < size and c < size:
        print('1사')
        visit += 0

    # 2사분면 처리
    elif r < size and c >= size:
        print('2사')
        visit += size * size
        c -= size

    # 3사분면 처리
    elif r >= size and c < size:
        print('3사')
        visit += size * size * 2
        r -= size
    # 4사분면 처리
    else:
        print('4사')
        visit += size * size * 3
        r -= size
        c -= size
    print(visit)

print(visit)

