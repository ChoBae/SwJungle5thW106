# 4673 셀프넘버
check = [True] * 10001  # 조건 10000이하 초기값
# n으로 만들 수있는 생성값 
def d(n,check):
    tmp = n 
    for i in str(n):
        tmp += int(i)
    # 조건이 10000 이하
    if tmp > 10000:
        return 
    # 생성값 제외 후 재귀 
    check[tmp] = False
    d(tmp,check)
# 1~10000까지 탐색
for i in range(1, 10001):
    # check 값을 계속 업데이트 해가면서 제외시킴
    if check[i]:
        print(i)
        d(i,check)
        
