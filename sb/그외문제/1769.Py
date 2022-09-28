# 1769 3의 배수
# 1. x를 한자리의 숫자가 될때까지 변환한다(각 자리수를 합치는 과정) -> 2. 3의 배수인지 확인한다.
# x를 한자리의 숫자로 바꿔주는 재귀 과정
def oper1(num):
    global res  # 전역변수 설정
    # num의 길이(숫자자리)가 1보다 클때 
    if len(num) > 1:
        tmp = 0 # 자리별 숫자 총합
        res += 1    # 연산 횟수 카운트
        for n in num:   # 숫자 자리별로 탐색
            tmp += int(n)   # 총합 업데이트
        # 한자리의 숫자가 될때까지 재귀 처리
        oper1(str(tmp))
    # 한자리의 숫자가 되었을때 출력
    else:
        print(res)  # 연산 횟수 
        print(oper2(num))   # 3의 배수인지 체크해서 'Yes" or "NO"
        return
    

# 3의 배수 체크 함수
def oper2(num):
    if int(num) % 3 == 0:
        return "YES"
    else:
        return "NO"
        
x =input()  # 숫자 x
res = 0 # 변환 횟수 res
oper1(x)    # oper1 재귀 시작

## 처음 풀이 pypy3만 통과.
# def oper1(num):
#     if len(str(num)) == 1:
#         print(oper2(num))
#         return
#     tmp = 0
#     for n in str(num):
#         tmp += int(n)
#     print(tmp)
#     oper1(tmp)


# def oper2(num):
#     if num % 3 == 0:
#         return "YES"
#     else:
#         return "NO"


# x = int(input())
# oper1(x)
