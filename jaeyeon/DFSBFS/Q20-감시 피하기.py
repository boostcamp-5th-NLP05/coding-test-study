import sys

def input():
    return sys.stdin.readline().rstrip()

N = 0
answer = "NO"
visited = []
T_list = []
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 선생님이 특정 방향(dir_)에 대해서 학생이 있는지 확인하는 함수
def check_direction(map_, dir_, r, c):
    next_r = r + dr[dir_]
    next_c = c + dc[dir_]
    while next_r not in [-1, N] and next_c not in [-1, N]:
        if map_[next_r][next_c] == "O":
            break
        elif map_[next_r][next_c] == "S":
            return False
        else:
            next_r += dr[dir_]
            next_c += dc[dir_]

    return True

# 선생님이 모든 학생을 발견하지 못하는지 확인하는 함수
def check_able(map_):
    for T_element in T_list:
        r, c = T_element
        # 각 선생님의 동, 남, 서, 북 방향에서 학생이 보이는지 확인
        # 한 방향이라도 보이면 False
        for dir_ in range(4):
            if not check_direction(map_, dir_, r, c):
                return False

    return True


def dfs(map_, depth):
    global answer
    # answer가 이미 YES면 더 볼 필요 없으므로 반환
    if answer == "YES":
        return

    # 깊이가 3이라는 뜻은 장애물 3개를 설치했다는 뜻이므로 조건에 맞는 맵인지 체크
    if depth == 3:
        if check_able(map_):
            answer = "YES"
        return

    else:
        for r in range(N):
            for c in range(N):
                if map_[r][c] == "X" and not visited[r][c]:
                    # 백트래킹을 활용하여 장애물 세우기
                    map_[r][c] = "O"
                    visited[r][c] = True
                    dfs(map_, depth + 1)
                    map_[r][c] = "X"
                    visited[r][c] = False
    return 0


if __name__ == "__main__":
    N = int(input())
    map_ = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        row = list(input().split())
        for c, val in enumerate(row):
            if val == "T":
                T_list.append([r, c])
        map_.append(row)
    dfs(map_, 0)
    print(answer)


# 27분 28초
# 백준 정답, 메모리: 116108 KB, 시간: 192 ms
