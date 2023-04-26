import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수(n)과 간선의 개수(m) 입력
n, m = map(int,input().split())

# 2차원 리스트 (그래프 표현) 만들고, 무한대로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # 등수가 a < b 이므로 1만큼 더해주면서 순위의 역순 결과가 나오도록 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# a를 기준으로 a번째열과 a번째 행을 보있을 때 다른 숫자들과 순위차이가 모두 존재한다면 a의 순위를 알 수 있음
for a in range(1, n + 1):
    temp = graph[a]
    for b in range(1, n + 1):
        if graph[b][a] == INF:
            graph[b][a] = 0 #순위차이를 모른다는 의미
        if temp[b] == INF:
            temp[b] = 0
        temp[b] += graph[b][a] 
    if 0 not in temp[:a] and 0 not in temp[a+1:]:
        result += 1
print(result)