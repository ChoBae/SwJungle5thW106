# # 2557
# print("Hello World!")


# #10869
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)


# # 2588
# A = int(input())
# B = input()

# # 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
# AxB2 = A * int(B[2])
# AxB1 = A * int(B[1])
# AxB0 = A * int(B[0])
# AxB = A * int(B)

# print(AxB2, AxB1, AxB0, AxB, sep='\n')


# #9498
# a = int(input())

# if 90<= a and a <= 100:
#     print("A")
# elif 80<= a and a <= 89:
#     print("B")
# elif 70<=a and a<=79:
#     print("C")
# elif 60<=a and a<=69:
#     print("D")
# else:
#     print("F")


# # 2753
# year =  int(input())

# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print(1)
# else:
#     print(0)


# #1085
# x, y, w, h = map(int, input().split())
# ary = []
# ary.append(x)
# ary.append(w-x)
# ary.append(y)
# ary.append(h-y)

# print(sorted(ary)[0])


# #2739
# a = int(input())

# for i in range(1, 10):
#     print(f"{a} * {i} = {a*i}")


# #10950
# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     print(A+B)


# #2438
# n = int(input())

# for i in range(1, n+1):
#     print("*"*i)


# #10871
# N, X = map(int, input().split())
# tmp = list(map(int, input().split()))
# for a in tmp:
#     if a < X:
#         print(a, end=" ")


# #2562
# tmp = 0
# idx = 0
# for i in range(1, 10):
#     a = int(input())
#     if tmp < a:
#         tmp = a
#         idx = i

# print(tmp)
# print(idx)


# #8958
# T = int(input())
# for _ in range(T):
#     tmp = input()
#     p = 0
#     ans = 0
#     for a in tmp:
#         if a == 'O':
#             p += 1
#         else:
#             p = 0
#         ans += p

#     print(ans)


# #4344
# #round함수는 끝의 0을 생략해버린다.
# for _ in range(int(input())):
#     ary = list(map(int,input().split()))
#     N = ary[0]
#     cnt = 0
#     for i in range(1, len(ary)):
#         if ary[i] > (sum(ary)-N)/N:
#             cnt += 1
#     print(f"{cnt/N*100:.3f}%")


# #2577
# # 딕셔너리 이용 풀이
# A = int(input())
# B = int(input())
# C = int(input())
# a = str(A*B*C)

# data = dict()
# for i in range(0, 10):
#     data[str(i)] = 0

# for num in a:
#     data[num] += 1

# for val in list(data.values()):
#     print(val)

# #일반 배열 이용 풀이
# a=int(input())
# b=int(input())
# c=int(input())

# idx = list()
# for i in range(0,10):
# 	idx.append(0)
# res = str(a*b*c)
# for i in range(0, len(res)):
# 	idx[int(res[i])] += 1
# for i in range(0, len(idx)):
# 	print(idx[i])

# #count 내장함수 사용 풀이
# a = int(input())
# b = int(input())
# c = int(input())
# tmp = a * b * c
# for i in range(9):
#     print(str(tmp).count(str(i)))


# #15596
# ans = sum(a)


# #11654
# asc = input()
# print(ord(asc))


# # 2675
# n = int(input())

# for _ in range(n):
#     cnt, word = input().split()
#     for x in word:
#         print(x*int(cnt), end='')
#     print()


# #1152
# a = list(input().split())
# print(len(a))


# #2908
# a, b = input().split()
# if a[::-1] > b[::-1]:
#     print(a[::-1])
# else:
#     print(b[::-1])


# #2869
# #1번 풀이
# #마지막으로 올라가기 전날 까지 세고,
# #올라갔다가 도착하면 print.
# #내용은 같은데 2번 방법이 더 깔끔함.
# import math
# A, B, V = map(int, input().split())
# tmp = (V-A)%(A-B)
# while True:
#     tmp = tmp - A
#     if tmp <= 0:
#         print(math.ceil((V-A)/(A-B)) + 1)
#         break
#     tmp = tmp + B

# #2번 풀이
# import math
# A, B, V = map(int, input().split())
# day = (V - B) / (A - B)
# print(math.ceil(day))


# #1978
# #1번 방법
# #소수는 약수가 두개이므로
# #약수의 갯수를 구해서 약수가 2개인 값의 수를 센다.
# T = int(input())
# ary = list(map(int, input().split()))
# #소수: 약수로 1과 자기 자신만을 갖는 수.
# res = 0
# for num in ary:
#     idx = 1
#     count = 0
#     while idx <= num:
#         if num % idx == 0:
#             count += 1
#         idx += 1
#     if count == 2:
#         res += 1
# print(res)

# #2번 방법
# n = int(input())
# ary = list(map(int, input().split()))
# count = 0

# for i in ary:
#     for j in range(2, i+1):
#         if n != 1:
#             if i != j and i % j == 0:
#                 break

#             if j == i:
#                 count += 1
#                 break

# print(count)


# #9020
# #다시해보기
# #시간초과 났던 코드
# def is_prime_number(x):
#     # 2부터 (x - 1)까지의 모든 수를 확인하며
#     for i in range(2, x):
#         # x가 해당 수로 나누어떨어진다면
#         if x % i == 0:
#             return False # 소수가 아님
#     return True # 소수임


# T = int(input())
# for _ in range(T):
#     num = int(input())
#     ary = []
#     for i in range(2, num):
#         if is_prime_number(i):
#             ary.append(i)

#     # print(ary)
#     tmp=[]
#     for j in range(0, len(ary)):
#         for k in range(j, len(ary)):
#             # print(j, k)
#             if ary[j] + ary[k] == num:
#                 tmp.append((abs(ary[k]-ary[j]), ary[j], ary[k]))
    
#     res = min(tmp)
#     print(f'{res[1]} {res[2]}')


# #정답 코드
# sosu = [0 for i in range(10001)]
# sosu[1] = 1

# for i in range(2, 98):
#     for j in range(i * 2, 10001, i):
#         sosu[j] = 1

# t = int(input())

# for i in range(t):
#     a = int(input())
#     b = a // 2
#     for j in range(b, 1, -1):
#         if sosu[a - j] == 0 and sosu[j] == 0:
#             print(j, a - j)
#             break
    

# #1065
# num = int(input())
# hansu = 0

# for n in range(1, num+1) :
#     if n <= 99 : # 1부터 99까지는 모두 한수
#         hansu += 1 
    
#     else :     
#         nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
#         if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
#             hansu+=1

# print(hansu)


# #2628

# x, y = map(int, input().split())
# T = int(input())
# x_ary = [0, x]
# y_ary = [0, y]
# for _ in range(T):
#     tmp = list(map(int, input().split()))
#     if tmp[0] == 0:
#         y_ary.append(tmp[1])
#     else:
#         x_ary.append(tmp[1])

# x_ary.sort()
# y_ary.sort()

# subx_max = 0
# suby_max = 0

# for i in range(len(x_ary)-1):
#     subx_max = max(subx_max, x_ary[i+1] - x_ary[i])
# for i in range(len(y_ary) -1):
#     suby_max = max(suby_max, y_ary[i+1] - y_ary[i])

# print(subx_max * suby_max)


# #10872
# # for 문 사용 풀이
# N = int(input())
# res = 1
# for i in range(1, N+1):
#     res = res*i

# print(res)

# #재귀함수 풀이
# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num-1)

# N = int(input())
# print(factorial(N))



# #17478
# def recur(count):  
#     print("____" * (num-count) +  "\"재귀함수가 뭔가요?\"")

#     if count == 0:
#         print("____" * (num-count) + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
#         return

#     print("____" * (num-count) +  "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
#     print("____" * (num-count) +  "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#     print("____" * (num-count) +  "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    
#     count -= 1
#     recur(count)

#     print("____" * (num-count) + "라고 답변하였지.")

# num = int(input())
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# recur(num)
# print("라고 답변하였지.")


# 5568
# # 순열 이용하는 방법
# from itertools import permutations
# n = int(input())
# k = int(input())
# cards = []
# for _ in range(n):
#     cards.append(int(input()))
# # print(cards)

# sets = set([])
# for i in permutations(cards, k):
#     a = ''
#     for j in range(len(i)):
#         a += str(i[j])
#     if a not in sets:
#         sets.add(a)

# # print(sets)
# print(len(sets))


# #재귀함수 이용하는 방법
# n = int(input())
# k = int(input())
# cards = [int(input()) for _ in range(n)]
# sets = set([])
# used = [0]*len(cards)

# def perm(arr, k):
#     if k==len(cards):
#         sets.add(''.join(map(str, arr)))
#         # 
#         print(sets)
#         # print(len(sets))
#         return 
    
#     for i in range(len(cards)):
#         if not used[i]:
#             used[i] = 1
#             arr.append(cards[i])
#             perm(arr, k+1)
#             arr.pop()
#             used[i] = 0

# perm([], 0)






# #1914
# # 다시
# N = int(input())

# #start_peg에서 end_peg으로 n개 원판을 옮기려면
# def HANOI(start_peg, other_peg, end_peg, cnt):
#     if cnt == 0:
#         return 

#     #H(n-1)
#     #start_peg에서 other_peg으로 n-1개 원판을 옮김.
#     HANOI(start_peg, end_peg, other_peg, cnt - 1)

#     #H(n)
#     #H(1) = 1
#     #start_peg에서 end_peg으로 1개 원판을 옮김.
#     print(start_peg, end_peg)

#     #H(n-1)
#     #other_peg에서 end_peg으로 n-1개 원판을 옮김.
#     HANOI(other_peg, start_peg, end_peg, cnt - 1)

# # 횟수 출력
# print(2**N-1)

# if N <= 20:
#     #H(n)
#     #start_peg에서 end_peg으로 n개 원판을 옮기기.
#     HANOI(1, 2, 3, N)


# #9663
# #다시 보기
# N = int(input())
# ans = 0
# col = [False]*N
# d1 = [False]*2*N
# d2 = [False]*2*N

# def backtracking(row):
#     global ans
#     if row == N:
#         ans += 1
#         return

#     for j in range(N if row else N//2):
#         if not col[j]and not d1[row-j] and not d2[row+j]:
#             col[j] = True
#             d1[row-j] = True
#             d2[row+j] = True

#             backtracking(row+1)

#             d2[row+j] = False
#             d1[row-j] = False
#             col[j] = False
    
# if N % 2:
#     backtracking(0)
#     ans *= 2

#     j = N//2
#     col[j] = d1[-j] = d2[j] = True
#     backtracking(1)
#     print(ans)

# else:
#     backtracking(0)
#     print(ans*2)



# #1074
# #다시 보기
# N, r, c = map(int, input().split())

# def sol(N, r, c):

# 	if N == 0:
# 		return 0
        
# 	return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))

# print(sol(N, r, c))
    

# #2750
# tmp = []
# for _ in range(int(input())):
#     tmp.append(int(input()))

# for i in sorted(tmp):
#     print(i)


# #2751
# import sys
# input = sys.stdin.readline
# tmp = []
# for _ in range(int(input())):
#     tmp.append(int(input()))

# for i in sorted(tmp):
#     print(i)


# # 10989
# # 메모리 초과 풀이
# import sys, heapq
# input = sys.stdin.readline
# print = sys.stdout.write
# tmp = []
# N = int(input())
# for _ in range(N):
#     heapq.heappush(tmp, int(input()))
    
# for _ in range(N):
#     print(str(heapq.heappop(tmp)) + '\n')


# # 이 문제는 for문 사용하여 푸는것과 어떻게 메모리 차이가 나는지 추후 보충 공부하기
# import sys
# n = int(sys.stdin.readline())
# countList = [0]*10001

# for i in range(n):
#     countList[int(sys.stdin.readline())] += 1

# for i in range(10001):
#     if countList[i] != 0:
#         for j in range(countList[i]):
#             print(i)


# #1181
# N = int(input())
# tmp = set([])
# for _ in range(N):
#     a = input()
#     tmp.add((len(a), a))

# for i in sorted(tmp):
#     print(i[1])


# #2309
# from itertools import combinations
# tmp = [int(input()) for _ in range(9)]

# for c in combinations(tmp, 7):
#     if sum(c) == 100:
#         for i in sorted(c):
#             print(i)
#         break


# #2798
# from itertools import combinations
# N, M =map(int, input().split())
# cards = list(map(int, input().split()))
# tmp = []
# for sets in combinations(cards, 3):
#     if M >= sum(sets):
#         # print(sets)
#         tmp.append([M-sum(sets), sum(sets)])

# tmp.sort()
# print(tmp[0][1])



# #10819
# from itertools import permutations
# N = int(input())
# l = list((map(int, input().split())))
# tmp = []
# sums = []

# for sets in permutations(l, N):
#     for i in range(0, N-1):
#         tmp.append(abs(sets[i]-sets[i+1]))
#     sums.append(sum(tmp))
#     tmp.clear()

# print(max(sums))

# #더 간단히 하면...
# from itertools import permutations

# N = int(input())
# A = list(map(int, input().split()))
# ans = -1
# for arr in set(permutations(A, N)):
#     ans = max(ans, sum(abs(arr[i-1] - arr[i]) for i in range(1, N)))

# print(ans)


# #10971
# #다시 보기
# import sys

# N = int(input()) #도시의 개수
# travel_cost = [list(map(int, input().split())) for _ in range(N)]
# min_value = sys.maxsize #출력할 최소값 정의


# def dfs_backtracking(start, next, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
#     global min_value

#     if len(visited) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
#         if travel_cost[next][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
#             min_value = min(min_value, value + travel_cost[next][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입
#         return

#     for i in range(N): #도시의 개수 만큼 반복문을 돈다.
#         #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
#         if travel_cost[next][i] != 0 and i not in visited and value < min_value: 
#             visited.append(i) #그 도시를 방문목록에 추가
#             dfs_backtracking(start, i, value + travel_cost[next][i], visited) #그 도시를 방문한다.
#             visited.pop() #방문을 완료했다면 방문목록 해제


# #도시마다(0~3) 출발점을 지정
# for i in range(N):
#     dfs_backtracking(i, i, 0, [i])

# print(min_value)



# #14888
# # # 순열 이용 - 시간초과/틀림
# # from itertools import permutations
# # N = int(input())
# # A = list(map(int, input().split()))
# # O = list(map(int, input().split()))

# # tmp = []
# # for i in range(4):
# #     if O[i] != 0:
# #         if i == 0:
# #             for _ in range(O[i]):
# #                 tmp.append("+") 
# #         elif i == 1:
# #             for _ in range(O[i]):
# #                 tmp.append("-")
# #         elif i == 2:
# #             for _ in range(O[i]):
# #                 tmp.append("*")
# #         elif i == 3:
# #             for _ in range(O[i]):
# #                 tmp.append("//")

# # # print(tmp)
# # find_max = 0
# # find_min = 123456789
# # for arr in permutations(tmp, len(tmp)):
# #     # print(arr)
# #     res = A[0]
# #     for j in range(0, len(A)-1):
# #         if arr[j] == "+":
# #             res += A[j+1]
# #         elif arr[j] == "-":
# #             res -= A[j+1]
# #         elif arr[j] == "*":
# #             res *= A[j+1]
# #         elif arr[j] == "//":
# #             res = int(res / A[j+1])
# #         # print(res)
# #     find_max = max(res, find_max)
# #     find_min = min(res, find_min)

# # print(find_max)
# # print(find_min)


# # 백트래킹 (Python3 통과, PyPy3도 통과)
# import sys

# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # +, -, *, //

# maximum = -1e9
# minimum = 1e9


# def dfs(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return

#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


# dfs(1, num[0], op[0], op[1], op[2], op[3])
# print(maximum)
# print(minimum)
    
    