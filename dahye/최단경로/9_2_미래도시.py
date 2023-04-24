import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수(n)과 간선의 개수(m) 입력
N, M = map(int,input().split())

# 2차원 리스트 (그래프 표현) 만들고, 무한대로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]


# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
    # A -> B로 가는 비용을 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 서로 이어졌으므로

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

X, K = map(int,input().split())

# 1번회사에서 K번회사 방문 후에 X번회사 방문의 최소시간
ans = graph[1][K] + graph[K][X]


if ans >= INF:
    print(-1)
else:
    print(ans)
