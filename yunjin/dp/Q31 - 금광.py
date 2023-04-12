import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for t in range(T):

    answer = 0

    N, M = map(int, input().split())

    map_ = [[] for i in range(N)]
    numbers = list(map(int, input().split()))

    # 초기화
    for r in range(N):
        for c in range(M):
            map_[r].append(numbers[r * M + c])

    # 누적합 배열
    prefix_map = [[0 for i in range(M)] for j in range(N)]

    for c in range(M):
        for r in range(N):

            # 첫 번째 열은 그대로 복사
            if c == 0:
                prefix_map[r][c] = map_[r][c]
            else:
                x = 0

                # 오른쪽 위, 오른쪽, 오른쪽위 -> 이전 열의 왼쪽 위, 왼쪽, 왼쪽 아래로 변경해서 함.
                for i in range(-1, 2, 1):
                    if 0 <= r + i < N: # 맵 내에 있을 때만 처리함
                        x = max(x, prefix_map[r+i][c-1])

                prefix_map[r][c] = x + map_[r][c] # 누적합 배열 갱신

    # 마지막 열에서 가장 큰 값 찾기
    for c in range(N):
        answer = max(answer, prefix_map[c][M-1])

    print(answer)