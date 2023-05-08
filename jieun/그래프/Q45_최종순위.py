# 백준 3665 정답: 35748 KB, 1144ms
import sys
from collections import deque

tcs = int(sys.stdin.readline().rstrip())

for _ in range(tcs):
    n = int(sys.stdin.readline().rstrip())
    edges = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    last = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n):  # len(last)
        for j in range(i + 1, n):
            edges[last[i]][last[j]] = 1
            # last_i 등수 < last_j 등수 이면 간선 last_i -> last_j

    m = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        # a,b 사이 기존 간선 제거하고 반대 방향 간선 추가
        edges[a][b] = 1 - edges[a][b]
        edges[b][a] = 1 - edges[b][a]

    ins = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ins[j] += edges[i][j]

    q = deque()
    cycle = False  # 위상정렬 시 사이클이 있으면 데이터에 일관성이 없는 것
    ans = []  # 올해 순위

    for i in range(1, n + 1):
        if ins[i] == 0:
            q.append(i)

    while q:
        if len(q) > 1:
            cycle = True
            break
        cur = q.popleft()
        ans.append(cur)
        for i in range(1, n + 1):
            if edges[cur][i] == 1:
                ins[i] -= 1
                if ins[i] == 0:
                    q.append(i)

    if cycle:
        print("?")
    elif len(ans) < n:
        print("IMPOSSIBLE")
    else:
        for a in ans:
            print(a, end=" ")
        print()
