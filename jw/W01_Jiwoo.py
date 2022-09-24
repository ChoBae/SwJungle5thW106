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
#딕셔너리 이용 풀이
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


#2675
# 배열 쓰는 방법
# T = int(input())
# for _ in range(T):
#     R, S = map(str, input().split())
#     res = []
#     for s in S:
#         print(s*int(R), end='')
#         for _ in range(int(R)):
#             res.append(s)
#     print(''.join(res))

# # 배열 따로 안쓰고 바로 출력하는 방법
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

# # #2번 풀이
# # #
# # import math
# # A, B, V = map(int, input().split())
# # day = (V - B) / (A - B)
# # print(math.ceil(day))


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

# # #2번 방법
# # n = int(input())
# # ary = list(map(int, input().split()))
# # count = 0

# # for i in ary:
# #     for j in range(2, i+1):
# #         if n != 1:
# #             if i != j and i % j == 0:
# #                 break

# #             if j == i:
# #                 count += 1
# #                 break

# # print(count)


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
# def is_prime(n):
#     if n == 1:
#         return False
#     for j in range(2, int(n**0.5) + 1):
#         if n % j == 0:
#             return False
#     return True


# for _ in range(int(input())):
#     num = int(input())

#     a, b = num//2, num//2
#     while a > 0:
#         if is_prime(a) and is_prime(b):
#             print(a, b)
#         else:
#             a -= 1
#             b += 1
    

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
# from itertools import combinations

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

# subtracted_r = []  #[4, 6]
# subtracted_c = []  #[2, 1, 5]

# for i in range(len(x_ary)-1):    # 0 1
#     subtracted_r.append(x_ary[i + 1] - x_ary[i])
# for i in range(len(y_ary) -1): # 0 1 2 
#     subtracted_c.append(y_ary[i+1]- y_ary[i])

# print(max(subtracted_r) * max(subtracted_c))


# #10872
# N = int(input())
# res = 1
# for i in range(1, N+1):
#     res = res*i

# print(res)


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


# # 5568
# from itertools import combinations, permutations
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


# #1914
# # 다시
# N = int(input())

# def HANOI(x, y, z, cnt):
#     if cnt == 0:
#         return

#     HANOI(x, z, y, cnt - 1)
#     print(x,z)
#     HANOI(y, x, z, cnt - 1)

# print((1 << N) - 1)
# if N <= 20:
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



#1074
#다시 보기
N, r, c = map(int, input().split())

def sol(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))

print(sol(N, r, c))
    

