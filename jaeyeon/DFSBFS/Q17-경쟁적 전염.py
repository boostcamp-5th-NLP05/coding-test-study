import sys
from collections import deque


def get_input():
    return map(int, sys.stdin.readline().rstrip().split())


if __name__ == "__main__":
    N, K = get_input()
    map_ = []
    # 나중에 사용할 바이러스 리스트 선언
    virus_list = [[] for _ in range(K + 1)]
    for r in range(N):
        row = list(get_input())
        for c, val in enumerate(row):
            if val != 0:
                virus_list[val].append([r, c])
        map_.append(row)
    S, X, Y = get_input()

    queue = deque()
    # 바이러스 번호 순대로 queue에 삽입
    for virus, positions in enumerate(virus_list):
        for position in positions:
            queue.append(position + [virus])

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    time = 0

    # 이 전에 업데이트 한 바이러스가 마지막 바이러스고,
    # 현재 바이러스가 첫번째 바이러스면 한 사이클(1초)가 돌았다는 뜻
    prev_virus = 0
    time = 0
    while queue:
        # BFS로 바이러스 퍼트리기
        cur_r, cur_c, virus_val = queue.popleft()
        if prev_virus == K and virus_val == 1:
            time += 1

        if time == S:
            break
        for r, c in zip(dr, dc):
            next_r = cur_r + r
            next_c = cur_c + c

            if next_r in [-1, N] or next_c in [-1, N]:
                continue

            if map_[next_r][next_c] != 0:
                continue

            map_[next_r][next_c] = virus_val
            queue.append([next_r, next_c, virus_val])

        prev_virus = virus_val

    print(map_[X - 1][Y - 1])


# 20분 6초
# 백준 정답, 메모리 121278 KB, 시간 224 ms
