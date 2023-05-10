import sys
from copy import deepcopy

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
# 반시계 방향 : +1


# 물고기들 이동시키는 함수
def fish_move(map_, fishes):
    for idx in range(1, 17):
        cur_r, cur_c, cur_dir = fishes[idx]
        if cur_r == -1:
            continue
        next_r = cur_r + dr[cur_dir]
        next_c = cur_c + dc[cur_dir]
        while next_r in [-1, 4] or next_c in [-1, 4] or map_[next_r][next_c][0] == 17:
            cur_dir = (cur_dir + 1) % 8
            next_r = cur_r + dr[cur_dir]
            next_c = cur_c + dc[cur_dir]

        if map_[next_r][next_c][0] == 0:
            map_[next_r][next_c] = [idx, cur_dir]
            map_[cur_r][cur_c] = [0, 0]
        else:
            change_fish = map_[next_r][next_c]
            map_[cur_r][cur_c] = change_fish
            map_[next_r][next_c] = [idx, cur_dir]

            fishes[idx] = [next_r, next_c, cur_dir]
            fishes[change_fish[0]] = [cur_r, cur_c, change_fish[1]]


total_eat = 0


def dfs(map_, fishes, cur_eat):
    global total_eat
    # dfs의 이전 depth에 영향 미치지 않게 copy 후 사용
    map_copy = deepcopy(map_)
    fishes_copy = deepcopy(fishes)
    # 물고기 이동
    fish_move(map_copy, fishes_copy)

    # 상어가 갈 수 있는 좌표 구하기
    shark_r, shark_c, shark_dir = fishes_copy[17]
    can_eat = []
    next_r = shark_r + dr[shark_dir]
    next_c = shark_c + dc[shark_dir]
    while 0 <= next_r < 4 and 0 <= next_c < 4:
        if map_copy[next_r][next_c] != 0:
            can_eat.append([next_r, next_c])

        next_r += dr[shark_dir]
        next_c += dc[shark_dir]

    # 갈 수 있는 좌표가 없다면 지금까지 먹은 것들 계산
    if not can_eat:
        total_eat = max(total_eat, cur_eat)
        return

    # 갈 수 있는 좌표마다 방문하면서 dfs 진행
    for eat in can_eat:
        next_r, next_c = eat
        eat_fish = map_copy[next_r][next_c]

        # 물고기 먹고 그 자리로 이동하기
        fishes_copy[17] = [next_r, next_c, eat_fish[1]]
        fishes_copy[eat_fish[0]] = [-1, -1, -1]
        map_copy[shark_r][shark_c] = [0, 0]
        map_copy[next_r][next_c] = [17, eat_fish[1]]

        dfs(map_copy, fishes_copy, cur_eat + eat_fish[0])

        # 백트래킹 : 물고기랑 상어 되돌려놓기
        fishes_copy[17] = [shark_r, shark_c, shark_dir]
        fishes_copy[eat_fish[0]] = [next_r, next_c, eat_fish[1]]
        map_copy[shark_r][shark_c] = [17, shark_dir]
        map_copy[next_r][next_c] = eat_fish


if __name__ == "__main__":
    map_ = []  # 각 좌표에 [번호, 방향]의 형태로 저장
    for _ in range(4):
        data = list(map(int, sys.stdin.readline().rstrip().split()))
        row = []
        for idx in range(0, 8, 2):
            row.append([data[idx], data[idx + 1] - 1])
        map_.append(row)

    fishes = [[-1, -1, -1] for _ in range(18)]  # [r, c, dir_]
    # 물고기들 순서대로 저장
    for r in range(4):
        for c in range(4):
            if r == 0 and c == 0:
                continue
            fishes[map_[r][c][0]] = [r, c, map_[r][c][1]]
    prev_start = map_[0][0][0]

    # [0, 0]에 상어 넣기, 번호는 17번으로
    shark_r, shark_c, shark_dir, shark_eat = 0, 0, map_[0][0][1], 0
    map_[0][0] = [17, shark_dir]
    fishes[17] = [0, 0, shark_dir]

    # 탐색 시작
    dfs(map_, fishes, prev_start)

    print(total_eat)
