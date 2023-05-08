import sys
from collections import deque
from heapq import heappush, heappop


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    cur_r, cur_c, cur_size, cur_eat = -1, -1, 2, 0

    n = int(input())
    map_ = []
    for r in range(n):
        row = list(map(int, input().split()))
        # 아기 상어 위치 찾기
        if cur_r == -1 and row.count(9) != 0:
            cur_r = r
            cur_c = row.index(9)
        map_.append(row)

    map_[cur_r][cur_c] = 0
    time = 0
    flag = True
    # 물고기 찾기 진행
    while flag:
        flag = False

        # BFS로 가까운 물고기 중 먹을 수 있는 물고기 찾기
        q = deque()
        q.append([cur_r, cur_c, 0])
        visited = [[False] * n for _ in range(n)]
        visited[cur_r][cur_c] = True
        can_eat = []
        min_dist = 0
        bfs_done = False
        while q and not bfs_done:
            r, c, dist = q.popleft()
            for dir_ in range(4):
                next_r = r + dr[dir_]
                next_c = c + dc[dir_]
                next_dist = dist + 1

                if next_r in [-1, n] or next_c in [-1, n]:
                    continue
                if map_[next_r][next_c] > cur_size:
                    continue
                if visited[next_r][next_c]:
                    continue
                if map_[next_r][next_c] != 0 and map_[next_r][next_c] < cur_size:
                    if not can_eat:
                        min_dist = next_dist
                    if next_dist > min_dist:
                        bfs_done = True
                        break

                    # 먹을 수 있는 물고기가 여러 마리일 수 있으므로 힙에 저장
                    heappush(can_eat, [next_dist, next_r, next_c])
                    flag = True

                visited[next_r][next_c] = True
                q.append([next_r, next_c, next_dist])

        if flag:
            # 조건에 맞는 물고기 pop
            next_dist, next_r, next_c = heappop(can_eat)
            map_[next_r][next_c] = 0
            cur_eat += 1
            if cur_eat == cur_size:
                cur_eat = 0
                cur_size += 1
            time += next_dist
            cur_r = next_r
            cur_c = next_c

    print(time)
