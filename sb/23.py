# 1065 한수 -> 풀이완료
# 100이하의 수중 100을 제외한 99개는 한수임 13(2), 45(1), 69(3)
# 100이상 부터 123(1), 135(2) 420(2)
n = int(input())    # 인풋 n
res = 0 # 결과값
for i in range(1,n+1):  # n까지의 수
    # 99까지는 모두 한수 
    if i < 100:
        res +=1
    # 100부터 제대로 체크
    else:
        check = True    # 한수 체크 불린형
        tmp = int(str(i)[0]) - int(str(i)[1])   # 첫번째인덱스의 수와 두번째인덱스의 수의 차이
        # 두번째 인덱스부터 마지막전까지의 인덱스 탐색
        for j in range(1, len(str(i))-1):
            # 구해놓은 차이와 다르다면 False 후 break
            if not tmp == int(str(i)[j]) - int(str(i)[j+1]):
                check = False
                break
        # 자릿수 모두 한수체크가 완료됐다면 결과값에 추가
        if check:
            res += 1
# 결과값 출력
print(res)