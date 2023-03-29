# 백준 14502 맞음: 34216 KB, 2968 ms, Python3
import sys
import itertools
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
total = N * M  # 총 칸 개수
map_ = []  # 0: 빈칸, 1: 벽, 2: 바이러스
# r행 c열 인덱스: r*M + c
for _ in range(N):  # 1차원으로 입력받는다.
    map_.extend(list(map(int, sys.stdin.readline().rstrip().split())))

# 2차원일 때 인접 칸 상대 위치
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(visited, start):
    # start(바이러스)에서 연결된 빈 칸들을 방문한다.
    q = deque()
    visited[start] = True
    q.append(start)
    while q:
        cur = q.popleft()
        for dr, dc in steps:
            # 인덱스에서 행과 열 계산
            nr = cur // M + dr
            nc = cur % M + dc
            if nr in [-1, N] or nc in [-1, M]:
                continue
            nidx = nr * M + nc
            if map_[nidx] == 0 and not visited[nidx]:
                # 아직 방문하지 않은 빈 칸이면 방문
                visited[nidx] = True
                q.append(nidx)


ans = 0

arr = [i for i in range(total)]
# [0, 1, ..., N*M-1] 중 3개를 고르는 조합
for one, two, three in itertools.combinations(arr, 3):
    # 고른 3 칸이 빈 칸이 아니면 다시 고른다.
    if map_[one] != 0 or map_[two] != 0 or map_[three] != 0:
        continue

    # 고른 3 칸을 벽으로 변환
    map_[one] = 1
    map_[two] = 1
    map_[three] = 1

    # 바이러스 칸에 대해 bfs를 돈다.
    visited = [False for _ in range(total)]
    for idx in range(total):
        if map_[idx] == 2:
            bfs(visited, idx)

    # 빈 칸인 개수를 세고 답을 갱신한다.
    cnt = 0
    for idx in range(total):
        if map_[idx] == 0 and not visited[idx]:
            cnt += 1
    ans = max(ans, cnt)

    # 고른 3 칸 빈 칸으로 원상복귀
    map_[one] = 0
    map_[two] = 0
    map_[three] = 0

print(ans)
