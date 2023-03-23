

# 회전 시키기.
def rotate_2d(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret


# 가운데 원본 자물쇠만 확인한다.
def check(array):
    num = len(array) // 3
    for i in range(num, num * 2): ## 가운데 원복 자물쇠 영역만 검사
        for j in range(num, num * 2):
            if array[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False

    # 자물쇠 새로 만들기. (자물쇠로 덮어 씌워준 공간만큼 확장)
    new_lock = [[2 for i in range(3 * len(lock))] for j in range(3 * len(lock))]

    # 기존 자물쇠 모양 삽입
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[i + len(lock)][j + len(lock)] = lock[i][j]

    # 새로운 자물쇠에서 열쇠를 완전 탐색한다. (0, 90, 180, 270 네 번 반복하도록 한다.)
    for i in range(4):
        for mr in range(0, 2 * len(lock) + 1, 1):
            for mc in range(0, 2 * len(lock) + 1, 1):

                # 새로운 자물쇠에 열쇠를 덧덴다.
                for a in range(len(key)):
                    for b in range(len(key)):
                        new_lock[a + mr][b + mc] += key[a][b]

                # 이 때 자물쇠의 모든 칸이 1 이라면 성공이다.
                if check(new_lock):
                    return True

                # 원복한다.
                for a in range(len(key)):
                    for b in range(len(key)):
                        new_lock[a + mr][b + mc] -= key[a][b]

        # 열쇠 회전.
        key = rotate_2d(key)

    return answer