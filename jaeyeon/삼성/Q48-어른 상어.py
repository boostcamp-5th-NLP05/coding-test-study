import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 다음에 갈 수 있는 위치 구하기
def move_pos(N, map_, shark_pos, shark_moves, shark_num):
    cur_r, cur_c = shark_pos
    for dir_ in shark_moves:
        dr, dc = moves[dir_]
        next_r = cur_r + dr
        next_c = cur_c + dc
        if next_r in [-1, N] or next_c in [-1, N]:
            continue
        if map_[next_r][next_c] != 0:
            continue
        return [next_r, next_c, dir_]

    for dir_ in shark_moves:
        dr, dc = moves[dir_]
        next_r = cur_r + dr
        next_c = cur_c + dc
        if next_r in [-1, N] or next_c in [-1, N]:
            continue
        if map_[next_r][next_c] == shark_num:
            return [next_r, next_c, dir_]


if __name__ == "__main__":
    N, M, k = map(int, input().split())
    cur_pos = [[-1, -1] for _ in range(M + 1)]
    map_ = []

    # 일정 시간이 지나면 없어지는 처리할 수 있게 queue 리스트 구현
    scent_list = [deque() for _ in range(M + 1)]
    for r in range(N):
        row = list(map(int, input().split()))
        map_.append(row)
        for c in range(N):
            if row[c] != 0:
                cur_pos[row[c]] = [r, c]
                scent_list[row[c]].append([r, c])

    # 상어들의 방향 우선 순위를 저장해둘 배열 생성
    dir_map = [[] for _ in range(M + 1)]
    cur_dir = list(map(int, input().split()))
    cur_dir = [dir_ - 1 for dir_ in cur_dir]
    cur_dir = [-1] + cur_dir
    for shark_idx in range(M + 1):
        if shark_idx == 0:
            continue
        dir_list = []
        for _ in range(4):
            dir_row = list(map(int, input().split()))
            dir_row = [dir_ - 1 for dir_ in dir_row]
            dir_list.append(dir_row)
        dir_map[shark_idx] = dir_list

    live_shark = M
    time = 0
    while live_shark > 1 and time < 1000:
        time += 1
        to_go = [[-1, -1]]

        # 각 상어들이 다음에 이동할 위치 구하기
        for idx in range(1, M + 1):
            if cur_pos[idx] == [-1, -1]:
                to_go.append([-1, -1, [-1, -1]])
                continue
            to_go.append(
                move_pos(N, map_, cur_pos[idx], dir_map[idx][cur_dir[idx]], idx)
            )

        # 상어 이동하기
        for shark_idx, next_pos in enumerate(to_go):
            if shark_idx == 0:
                continue
            next_r, next_c, next_dir = next_pos
            if next_r == -1:
                continue

            if map_[next_r][next_c] not in [0, shark_idx]:
                cur_pos[shark_idx] = [-1, -1]
                live_shark -= 1
            else:
                map_[next_r][next_c] = shark_idx
                cur_pos[shark_idx] = [next_r, next_c]
                cur_dir[shark_idx] = next_dir
                scent_list[shark_idx].append([next_r, next_c])

        # 냄새 없애기
        if time >= k:
            for shark_idx in range(1, M + 1):
                if scent_list[shark_idx]:
                    remove_scent_pos = scent_list[shark_idx].popleft()
                    rm_r, rm_c = remove_scent_pos
                    if [rm_r, rm_c] not in cur_pos:
                        map_[rm_r][rm_c] = 0

    if time == 1000:
        print("-1")
    else:
        print(time)
