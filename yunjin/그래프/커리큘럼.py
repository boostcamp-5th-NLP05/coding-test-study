import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
graph_cost = [[] for i in range(N + 1)]  # 강의별 시간 저장

for i in range(1, N + 1):
    numbers = list(map(int, input().split()))
    graph_cost[i] = numbers[0] # 첫째꺼는 강의의 시간임.
    for j in range(1, len(numbers) - 1):
        graph[numbers[j]].append(i) # 선수강 해야 하는 강의 연결하기
        indegree[i] += 1

def topology_sort():
    result = []
    q = deque()

    # 진입차수 0 인 것 다 넣기.
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append((i, graph_cost[i]))

    while q:
        now, now_cost = q.popleft()
        result.append((now, now_cost)) # result 에 넣어주기

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append((i, now_cost+graph_cost[i])) # 시간 더해서 넣어주기

    return result


# 위상 정렬 실행
answer = topology_sort()

# 강의 번호 순으로 나열하기.
answer.sort()

for ans in answer:
    print(ans[1])

