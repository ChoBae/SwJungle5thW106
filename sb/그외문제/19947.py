# 19947 투자의 귀재
# 1번 재귀풀이 안됨..
oper = [(1, 0.05), (3, 0.20), (5, 0.35)]


def rec(year, sum):
    global res
    if year == 0:
        res = max(res, sum)
        return
    for i in range(3):
        y, p = oper[i][0], oper[i][1]
        if year-y >= 0:
            rec(year-y,int(sum + sum* p))

res = -10e9
h, y = map(int, input().split())
rec(y, h)
print(res)


# # 2번 dp풀이
# h, y = map(int, input().split())    # 가진돈 h, 투자기간 y
# dp = [0 for i in range(y+1)]    # dp 테이블 생성
# dp[0] = h   # dp 첫 시작 가진돈.

# for i in range(1, y+1):
#     # 5년차 이상일때 a, b, c 모두 고려해줌
#     if i >= 5:
#         dp[i] = max(dp[i-1]*1.05, dp[i-3]*1.2, dp[i-5]*1.35)
#     # 3년차 이상일떄 a,b 고려
#     elif i >= 3:
#         dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.2)
#     # 3년 이하 일때는 a 투자만 가능
#     else:
#         dp[i] = dp[i - 1] * 1.05
#     # 이자받는 금액 소수점 제거
#     dp[i] = int(dp[i])
# # 결과값 출력
# print(int(dp[y]))
