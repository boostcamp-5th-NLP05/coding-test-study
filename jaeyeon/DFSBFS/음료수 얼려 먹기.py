dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ice_map = []
N, M = 0, 0


def dfs(r, c):
    cur_r, cur_c = r, c
    # 현재 지점을 1로 만들어주기 때문에 재방문 못함
    ice_map[cur_r][cur_c] = 1
    
    # 현재 지점부터 네 방향을 돌며 깊이 우선 탐색 진행
    for r, c in zip(dr, dc):
        next_r = cur_r + r
        next_c = cur_c + c
        if next_r in [-1, N] or next_c in [-1, M]:
            continue
        if ice_map[next_r][next_c] == 1:
            continue
        dfs(next_r, next_c)

    # 첫 dfs가 실행되고 끝나면 하나의 얼음이 만들어지므로 1 반환
    return 1


if __name__ == "__main__":
    N, M = map(int, input().split())

    for _ in range(N):
        row = [int(c) for c in input()]
        ice_map.append(row)

    answer = 0
    for r in range(N):
        for c in range(M):
            if ice_map[r][c] == 0:
                answer += dfs(r, c)

    print(answer)

# 15분 33초
