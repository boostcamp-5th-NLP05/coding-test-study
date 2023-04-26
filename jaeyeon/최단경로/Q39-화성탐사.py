import sys
from heapq import heappop, heappush


def input():
    return sys.stdin.readline().rstrip()


INF = int(1e9)

if __name__ == "__main__":
    T = int(input())
    answers = []
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    for _ in range(T):
        # 입력 받기
        N = int(input())
        map_ = []
        for _ in range(N):
            map_.append(list(map(int, input().split())))

        # 거리 저장 배열 선언 및 초기화
        dist_map = [[INF] * (N) for _ in range(N)]
        dist_map[0][0] = map_[0][0]

        # 힙큐 선언 및 초기값 push
        hq = []
        heappush(hq, [map_[0][0], 0, 0])

        # 다익스트라 알고리즘 수행
        while hq:
            cur_dist, cur_r, cur_c = heappop(hq)
            if cur_dist > dist_map[cur_r][cur_c]:
                continue

            # 인접한 네 방향에 대해서 탐색 진행
            for dir_ in range(4):
                next_r = cur_r + dr[dir_]
                next_c = cur_c + dc[dir_]
                if next_r in [-1, N] or next_c in [-1, N]:
                    continue

                next_dist = map_[next_r][next_c]
                new_dist = cur_dist + next_dist
                if new_dist < dist_map[next_r][next_c]:
                    dist_map[next_r][next_c] = new_dist
                    heappush(hq, [new_dist, next_r, next_c])

        # 마지막 칸의 값 저장
        answers.append(dist_map[N - 1][N - 1])

    for answer in answers:
        print(answer)
