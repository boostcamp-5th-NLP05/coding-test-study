# 백준 19236 정답: 34288 KB, 96 ms
import sys
from collections import deque
import copy

dir_step = [
    (-1, 0),  # 0: 위
    (-1, -1),  # 1: 왼쪽 위
    (0, -1),  # 2: 왼쪽
    (1, -1),  # 3: 왼쪽 아래
    (1, 0),  # 4: 아래
    (1, 1),  # 5: 오른쪽 아래
    (0, 1),  # 6: 오른쪽
    (-1, 1),  # 7: 오른쪽 위
]
dir_sym = ["↑", "↖", "←", "↙", "↓", "↘", "→", "↗"]  # 디버그 출력 용

original_map = [[] for _ in range(4)]  # 4x4 행렬. 각 칸에 (물고기, 방향)
for r in range(4):
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(0, 8, 2):
        original_map[r].append((l[i], l[i + 1] - 1))
        # 방향 인덱스 0부터 시작하게 수정


def print_map(a_map):
    # 디버그 용 맵 출력
    for l in a_map:
        for f, d in l:
            print(f"{f}{dir_sym[d]}", end=" ")
        print()
    print()


# 모든 물고기가 이동한 새로운 맵 반환
def move_fish(cur_map, shark_r, shark_c):
    new_map = copy.deepcopy(cur_map)

    # 각 물고기의 위치 찾기
    pos = [(-1, -1) for _ in range(17)]
    for i in range(4):
        for j in range(4):
            if i == shark_r and j == shark_c:  # 상어
                continue
            if new_map[i][j][0] == 0:  # 빈칸
                continue
            pos[new_map[i][j][0]] = (i, j)

    # 번호 순으로 물고기 이동
    for r, c in pos:
        if r == -1:
            continue  # 물고기 없음
        d = new_map[r][c][1]  # 방향
        for _ in range(8):
            nr = r + dir_step[d][0]
            nc = c + dir_step[d][1]
            if (
                nr < 0
                or nr >= 4
                or nc < 0
                or nc >= 4
                or (nr == shark_r and nc == shark_c)
            ):  # 범위를 벗어나거나 상어를 만나면
                d = (d + 1) % 8  # 반시계 방향 45도 회전
                continue

            # swap
            tmp = new_map[nr][nc]
            new_map[nr][nc] = (new_map[r][c][0], d)
            new_map[r][c] = tmp
            pos[tmp[0]] = (r, c)
            # 현재 물고기 pos 값은 갱신 안 해줘도 됨. 나중에 사용 안 하기 때문.
            break

    return new_map


ans = original_map[0][0][0]
q = deque()
# (map, fish_sum, shark_r, shark_c)
q.append((original_map, ans, 0, 0))

while q:
    current_map, fish_sum, shark_r, shark_c = q.popleft()
    ans = max(ans, fish_sum)

    new_map = move_fish(current_map, shark_r, shark_c)  # 모든 물고기가 이동한 새로운 맵
    d = new_map[shark_r][shark_c][1]  # 방향
    new_map[shark_r][shark_c] = (0, -1)  # 상어 있는 곳 빈칸으로 변경

    while True:  # 상어가 먹을 수 있는 모든 경우 큐에 넣기
        shark_r += dir_step[d][0]
        shark_c += dir_step[d][1]
        if shark_r < 0 or shark_r >= 4 or shark_c < 0 or shark_c >= 4:
            break
        if new_map[shark_r][shark_c][0] > 0:  # 물고기 존재
            q.append(
                (new_map, fish_sum + new_map[shark_r][shark_c][0], shark_r, shark_c)
            )

print(ans)
