# 백준 19237 정답: 34436 KB, 248 ms
import sys
from collections import defaultdict

### 입력
N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
tmp_dir = list(map(int, sys.stdin.readline().rstrip().split()))  # 초기 상어 방향
priority = [[] for _ in range(M + 1)]  # 상어별 방향별 우선순위
for i in range(1, M + 1):
    priority[i].append([])  # 방향 번호 0번 패딩
    priority[i].extend(
        [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(4)]
    )

# 1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽
steps = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
step_to_dir = {(-1, 0): 1, (1, 0): 2, (0, -1): 3, (0, 1): 4}

time = 0  # 현재 시각
time_arr = [[-1 for _ in range(N)] for _ in range(N)]  # 최근 냄새가 뿌려진 시각
shark = [(-1, -1, -1) for _ in range(M + 1)]  # (row, col, 방향)

## 초기 격자 보면서 time_arr, shark 채우기
for r in range(N):
    for c in range(N):
        x = arr[r][c]
        if x > 0:
            shark[x] = (r, c, tmp_dir[x - 1])
            time_arr[r][c] = time


def get_new_pos():
    ## 상어가 이동할 칸 반환
    new_pos = defaultdict(list)
    for i in range(1, M + 1):
        r, c, d = shark[i]
        if r == -1:
            continue  # 제거된 상어
        found = False

        # 냄새 없는 칸 탐색
        for nd in priority[i][d]:
            nr = r + steps[nd][0]
            nc = c + steps[nd][1]
            if nr in [-1, N] or nc in [-1, N]:
                continue
            if time - time_arr[nr][nc] > K or time_arr[nr][nc] == -1:
                # 현재 시각과 냄새 묻은 시각 차이가 K보다 크면 or 냄새가 묻지 않았으면
                new_dir = step_to_dir[(nr - r, nc - c)]
                new_pos[(nr, nc)].append((i, new_dir))
                found = True
                break

        if not found:
            # 자기 냄새 칸 탐색
            for nd in priority[i][d]:
                nr = r + steps[nd][0]
                nc = c + steps[nd][1]
                if nr in [-1, N] or nc in [-1, N]:
                    continue
                if arr[nr][nc] == i:
                    # 자기 냄새 묻은 칸이면
                    new_dir = step_to_dir[(nr - r, nc - c)]
                    new_pos[(nr, nc)].append((i, new_dir))
                    break
    return new_pos


while True:
    time += 1

    new_pos = get_new_pos()  # new_pos: {칸: [(상어1, 방향1), (상어2, 방향2), ...]}

    ## arr에 상어 이동 반영 + 한 칸에 여러 마리 상어 있으면 처리
    for (r, c), i in new_pos.items():
        arr[r][c] = i[0][0]
        time_arr[r][c] = time
        shark[i[0][0]] = (r, c, i[0][1])
        for j, _ in i[1:]:
            # 첫 번째 상어(번호가 가장 작은 상어) 외 상어는 제거
            shark[j] = (-1, -1, -1)

    ## 1번 상어만 격자에 남아 있는지 확인
    num = 0
    for i in range(1, M + 1):
        if shark[i][0] > -1:
            num += 1

    if num == 1:
        break
    if time >= 1000:  # (틀린 이유) >가 아니었다!
        time = -1
        break

print(time)
