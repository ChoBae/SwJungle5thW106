# # 10971 외판원 순회 2

# import sys
# n = int(input())    # 도시의 수 n
# t = [list(map(int, input().split())) for _ in range(n)]  # 도시의 수만큼 비용행렬
# def sol(start, end, target , sum, visited):
#     global MinRes
#     if False not in visited:
#         sum += t[end][target]
#         MinRes = min(MinRes, sum)
#         return

#     for i in range(len(t[end])):
#         if not visited[i] and t[end][i] != 0:
#             visited[start] = True
#             print(start, end, sum)
#             print(visited)
#             sol(end, i, target, sum+t[end][i],visited)


# for i in range(n):
#     for j in range(n):
#         if t[i][j] !=0:
#             print(i,j)
#             visited = [False] * n
#             MinRes = 10e9
#             visited[i] = True
#             sol(i, j, i, t[i][j],visited)
# print(MinRes)


import sys


N = int(input())  # 도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = 10e9 # 출력할 최소값 정의


def dfs_backtracking(start, next, value, visited):  # 시작도시번호,다음도시번호,비용,방문 도시
    global min_value

    if len(visited) == N:  # 만약 방문한 도시가 입력받은 도시의 개수라면
        # 마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
        if travel_cost[next][start] != 0:
            # 더한 값을 저장되어있는 최소값과 비교해서 대입
            print(value + travel_cost[next][start])
            min_value = min(min_value, value + travel_cost[next][start])
        return
    for i in range(N):  # 도시의 개수 만큼 반복문을 돈다.
        # 만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if travel_cost[next][i] != 0 and i not in visited and value < min_value:
            
            visited.append(i)  # 그 도시를 방문목록에 추가
            print(visited)
            # 그 도시를 방문한다.
            dfs_backtracking(start, i, value + travel_cost[next][i], visited)
            visited.pop()  # 방문을 완료했다면 방문목록 해제


# 도시마다(0~3) 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)
