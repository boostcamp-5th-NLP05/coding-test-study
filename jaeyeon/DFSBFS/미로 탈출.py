from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())

    map_ = []
    for _ in range(N):
        map_.append([int(c) for c in input()])
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 현재 지점과 depth를 함께 저장, 여기서의 depth는 한 지점까지의 최소 거리를 뜻함
    queue = deque([[0, 0, 1]])

    while len(queue) != 0:
        cur_r, cur_c, cur_depth = queue.popleft()
        if map_[cur_r][cur_c] == 0:
            continue
        
        # 현재 방문한 지점의 값이 1이라면 처음 방문하는 지점이므로 현재의 depth로 업데이트
        if map_[cur_r][cur_c] == 1:
            map_[cur_r][cur_c] = cur_depth

        for r, c in zip(dr, dc):
            next_r = cur_r + r
            next_c = cur_c + c

            # 범위 검사
            if next_r in [-1, N] or next_c in [-1, M]:
                continue

            # 값이 1인 지점만 방문 가능
            if map_[next_r][next_c] != 1:
                continue

            # 다음 방문 지점이 출구라면 그 전 지점의 값 + 1 을 반환 => 최소거리라는 뜻
            if next_r == N - 1 and next_c == M - 1:
                print(map_[next_r - r][next_c - c] + 1)
                break

            queue.append([next_r, next_c, cur_depth + 1])

# 27분 20초