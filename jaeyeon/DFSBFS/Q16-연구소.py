from itertools import combinations
import copy
from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())
    lab = []
    virus_list = []
    empty_list = []

    # 추후에 사용하도록 0과 2인 곳의 위치를 모두 저장
    for r in range(N):
        row = list(map(int, input().split()))
        lab.append(row)
        for c, val in enumerate(row):
            if val == 0:
                empty_list.append([r, c])
            elif val == 2:
                virus_list.append([r, c])

    # 벽을 세울 수 있는 조합을 모두 구하기
    empty_comb = combinations(empty_list, 3)

    answer = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    # 각 벽의 조합에 따라서 완전 탐색
    for empty_temp in empty_comb:
        lab_copy = copy.deepcopy(lab)
        virus_list_copy = copy.deepcopy(virus_list)
        # 벽 세우기
        for wall in empty_temp:
            r, c = wall
            lab_copy[r][c] = 1
        queue = deque(virus_list_copy)

        # 바이러스를 기준으로 BFS로 바이러스 퍼트리기
        while queue:
            cur_r, cur_c = queue.popleft()
            lab_copy[cur_r][cur_c] = 2

            for r, c in zip(dr, dc):
                next_r = cur_r + r
                next_c = cur_c + c

                if next_r in [-1, N] or next_c in [-1, M]:
                    continue

                if lab_copy[next_r][next_c] != 0:
                    continue

                queue.append([next_r, next_c])

        # 안전 구역 개수 세기
        safe_cnt = 0
        for row in lab_copy:
            safe_cnt += row.count(0)

        # 안전 구역의 최대 개수로 업데이트
        answer = max(answer, safe_cnt)

    print(answer)

# 14분 2초
