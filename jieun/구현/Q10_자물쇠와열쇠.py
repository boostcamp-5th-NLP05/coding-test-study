def solution(key, lock):
    key_len = len(key)  # 열쇠 한 변 길이
    lock_len = len(lock)  # 자물쇠 한 변 길이
    lock_start = key_len - 1  # 확장판에서 자물쇠가 시작하는 인덱스
    bar = key_len + lock_len - 1  # 확장판에서 자물쇠가 끝나는 인덱스 + 1

    def check(key_r, key_c):
        # 열쇠 왼쪽 위 칸이 확장판 (key_r, key_c)에 있을 때 가능한지 확인
        total_key_start = (key_r, key_c)  # 열쇠 왼쪽 위 칸의 확장판 인덱스
        total_key_end = (  # 열쇠 오른쪽 아래 칸의 확장판 인덱스
            key_r + key_len - 1,
            key_c + key_len - 1,
        )

        # 자물쇠 칸을 하나씩 확인한다.
        for i in range(0, lock_len):
            for j in range(0, lock_len):
                # 자물쇠 칸(i,j)의 확장판 인덱스(lr,lc)
                lr = i + lock_start
                lc = j + lock_start

                if (
                    total_key_start[0] <= lr
                    and lr <= total_key_end[0]
                    and total_key_start[1] <= lc
                    and lc <= total_key_end[1]
                ):  # 열쇠 칸과 자물쇠 칸이 겹쳐져 있는데 같은 값이면 False 반환.
                    if lock[i][j] == key[lr - key_r][lc - key_c]:
                        return False
                elif lock[i][j] == 0:
                    # 열쇠 칸과 자물쇠 칸이 겹쳐져 있지 않는데, 자물쇠 칸이 홈이면 False 반환
                    return False

        return True

    for _ in range(4):
        # 열쇠를 한 칸씩 움직이면서 자물쇠와 맞물리는지 확인
        for r in range(0, bar):
            for c in range(0, bar):
                if check(r, c):
                    return True

        # 시계방향 90도 회전
        new_key = []
        for c in range(0, key_len):
            new_row = []
            for r in range(key_len - 1, -1, -1):
                new_row.append(key[r][c])
            new_key.append(new_row)
        key = new_key

    return False
