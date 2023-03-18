N, M = map(int, input().split())
A, B, direction = map(int, input().split())
region = []
for _ in range(N):
    region.append(list(map(int, input().split())))

# visited[r][c]: (r,c)칸 방문했으면 True, 아니면 False
visited = [[False for _ in range(M)] for _ in range(N)]

# step[d]: d 방향을 바라보고 있을 때 걸음
step = [(-1, 0), (0, 1), (1, 0), (-1, 0)]
# step[0]: 북쪽, step[1]: 동쪽, step[2]: 남쪽, step[3]: 서쪽


def can_go(nr, nc):
    """(nr,nc)에 갈 수 있는지 반환"""
    # 맵 밖으로 나가는지 확인
    if nr < 0 or nr >= N or nc < 0 or nc >= M:
        return False
    # 바다이거나 방문한 칸인지 확인
    if region[nr][nc] != 0 or visited[nr][nc] != False:
        return False
    return True


# 현재 위치도 방문한 칸에 포함
ans = 1
visited[A][B] = True

# 캐릭터 움직임 시작
while True:
    back = True
    for i in range(4):
        # 반시계방향 direction 값 변화는 다음과 같다: 0 -> 3 -> 2 -> 1 -> 0
        direction = (direction - 1 + 4) % 4
        # 방문할 칸 (nr, nc)
        nr = A + step[direction][0]
        nc = B + step[direction][1]
        if can_go(nr, nc):
            back = False  # 뒤쪽 방향(매뉴얼 3) 볼 필요 없다.
            A = nr
            B = nc
            visited[nr][nc] = True
            ans += 1
            break

    # 네 방향 못 가서 뒤로 가기 시도
    if back:
        # 뒤쪽 방향: 0 <-> 2, 1 <-> 3
        direction = (direction + 2) % 4
        nr = A + step[direction][0]
        nc = B + step[direction][1]
        if can_go(nr, nc):
            A = nr
            B = nc
            visited[nr][nc] = True
            ans += 1
        else:
            break  # 뒤로도 못 가서 루프 탈출

print(ans)
