# 백준 18352 맞음: 100284 KB, 1456 ms, Python3
import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
edge = [[] for _ in range(N + 1)]  # 인덱스 1부터 시작
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    edge[A].append(B)

# 방문하지 않은 도시는 -1. 방문한 도시는 최단거리를 기록한다.
dist = [-1 for _ in range(N + 1)]
q = deque()

ans = []
dist[X] = 0
q.append(X)
while q:
    cur = q.popleft()
    if dist[cur] == K: # 거리가 K인 도시는 답에 넣고 다음 루프를 돈다.
        ans.append(cur)
        continue

    for nxt in edge[cur]:
        if dist[nxt] == -1:  # 방문하지 않은 도시만 탐색한다.
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for x in ans:
        print(x)
