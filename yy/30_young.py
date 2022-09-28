# 재귀함수 z 1074
def Z(n,r,c,q):
    half = 2**(n-1)
    global result
    quad = 0
    if n == 1:
        if r == 0 and c == 0:
            return
        elif r == 0 and c == 1:
            result += 1
        elif r == 1 and c == 0:
            result += 2
        elif r == 1 and c == 1:
            result += 3
        return
    elif r < half and c < half:
        quad = 1

    elif r < half and c >= half:
        quad = 2
        c -= half
    elif r >= half and c < half:
        quad = 3
        r -= half
    elif r >= half and c >= half:
        quad = 4
        r -= half
        c -= half

    result += (quad-1) * half**2
    # print(result)
    Z(n-1, r, c, result)

n, r, c = map(int, input().split())
result =0
Z(n, r, c, result)
print(result)