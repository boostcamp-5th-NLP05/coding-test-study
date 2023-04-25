import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))

INF = 1e9
graph = [[int(INF)] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


answer = 0

# 그래프에서 특정 성분이 INF 가 아니라는 것은 어떤 i -> j 가 연결 되어 있다는 것임. -> 대소 비교 가능함
# j -> i 가 연결 되어도 대소 비교 가능한 것이므로 둘 중 하나만 INF 아니면 됨.
# 특정 학생에 대해서 이런 경우가 N 명 있으면 순위를 알 수 있다. (본인포함)

for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == N:
        answer += 1

print(answer)