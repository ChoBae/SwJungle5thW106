# 9663 N-Queen -> pypy3 말고 풀이가 안되는듯? 

## 1번 풀이 Pypy3 통과 -> 책 풀이 그대로 
# n = int(input())

# pos= [0] * n
# flag_a = [False] * n
# flag_b = [False] * (n*2-1)
# flag_c = [False] * (n*2-1)
# res = 0
# def set(i):
#     global res
#     for j in range(n):
#         if (not flag_a[j] and not flag_b[i+j] and not flag_c[i-j]):
#             pos[i] = j
#             if i == n-1:
#                 res +=1 
#             else:
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j] = True
#                 set(i+1)
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j] = False

# set(0)
# print(res)

## 2번 풀이 
n = int(input())

ans = 0
row = [0] * n

# 퀸을 놓을수 있는지 체크 함수
def is_promising(x):
    # x까지 검사
    for i in range(x):
    
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)


n_queens(0)
print(ans)
