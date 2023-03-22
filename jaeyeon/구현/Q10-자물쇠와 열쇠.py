import copy

# 열쇠 회전 시키는 함수
def rotation(key):
    N = len(key)
    new_key = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][len(key) - i - 1] = key[i][j]

    return new_key


def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key) - 1

    # lock을 그대로 두고 열쇠와 비교하면 열쇠를 움직일 때 손실이 날 수 있으므로
    # 미리 lock에 패딩을 추가하기
    # 값을 3으로 초기화한 이유는 padding 부분에는 key가 걸쳐도 되기 때문에
    # lock과 key가 겹치는 것을 구분하기 위해서이다.
    # 만약 1로 초기화할 시 padding_map과 key를 더했을 때 2라는 값이 나오면
    # 그게 padding과 겹쳐진건지 lock과 겹쳐진건지 구분할 수 없다
    # 값을 정리하면 아래와 같다.
    # 0 : lock의 홈, 1 : lock의 돌기 또는 key의 홈 + lock의 돌기, 
    # 2 : lock의 돌기 + key의 돌기, 3 : padding, 4: padding + key의 돌기
    padding_map = [[3 for _ in range(N + 2 * M)] for _ in range(N + 2 * M)]
    for i in range(0, N):
        for j in range(0, N):
            padding_map[i + M][j + M] = lock[i][j]

    turn_cnt = 0
    while turn_cnt < 4 and not answer:
        turn_cnt += 1

        # padding map에서 key를 들고 순회해야함
        for i in range(N + M):
            for j in range(N + M):
                map_copy = copy.deepcopy(padding_map)

                # 순회하면서 padding map에 key의 값들을 더해주기
                for k_i in range(M + 1):
                    for k_j in range(M + 1):
                        map_copy[i + k_i][j + k_j] += key[k_i][k_j]

                # 패딩을 제외한 중간의 lock 부분의 값들만 리스트로 만들기
                val_list = [
                    map_copy[i][j]
                    for i in range(M, M + N)
                    for j in range(M, M + N)
                ]

                # 0은 lock에서 채워지지 않은 공간
                # 2는 lock과 key의 돌기가 겹쳐진 공간이므로 둘 다 없어야 자물쇠를 열 수 있는 것
                zeros = val_list.count(0)
                twos = val_list.count(2)
                if zeros == 0 and twos == 0:
                    answer = True

        # 열쇠 회전하고 처음으로 돌아가기
        key = rotation(key)

    return answer


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))


# 44분 28초
# 정확성 97점
