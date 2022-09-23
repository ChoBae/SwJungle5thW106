# ox퀴즈
t = int(input())
for _ in range(t):
    User_Input = input()
    cnt = 0
    res = 0
    for i in User_Input:
        if i == 'X':
            cnt = 0
        else:
            cnt += 1
            res += cnt
    print(res)
