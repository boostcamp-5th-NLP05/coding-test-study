import sys
from collections import deque

# input 중복으로 받는 부분 모두 함수화
def input():
    return list(map(int, sys.stdin.readline().rstrip().split()))


if __name__ == "__main__":
    N, L, R = input()
    map_ = []
    for _ in range(N):
        map_.append(input())
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 인구 이동이 일어나는 시간을 저장할 변수 answer
    answer = 0
    while True:
        # 매일 연합은 초기화 되므로 while문 내의 지역 변수로 선언
        union_map = [[-1 for _ in range(N)] for _ in range(N)]
        union_number = -1
        # 연합의 인구합과 수를 저장해둘 리스트 선언
        union_list = []
        for r in range(N):
            for c in range(N):
                # 값이 -1 이라는 뜻은 아직 연합에 소속되지 않았다는 뜻
                if union_map[r][c] == -1:
                    # 새로운 연합을 만들 때마다 union 번호 증가
                    union_number += 1
                    queue = deque([[r, c]])
                    union_map[r][c] = union_number

                    # 추후에 인구 이동을 편하게 하기 위해 미리 연합의 인구 합과 연합된 나라 개수 구하기
                    union_sum, union_cnt = map_[r][c], 1

                    # 현재 지역에서 인구 차이가 L 이상 R 이하인 지역을 모두 현재 연합으로 지정
                    while queue:
                        cur_r, cur_c = queue.popleft()

                        for dir_ in range(4):
                            next_r = cur_r + dr[dir_]
                            next_c = cur_c + dc[dir_]

                            if next_r in [-1, N] or next_c in [-1, N]:
                                continue

                            if union_map[next_r][next_c] != -1:
                                continue
                            # 조건에 맞는 나라 찾으면 바로 연합에 포함 시키고 sum, cnt 업데이트
                            if L <= abs(map_[cur_r][cur_c] - map_[next_r][next_c]) <= R:
                                queue.append([next_r, next_c])
                                union_map[next_r][next_c] = union_number
                                union_sum += map_[next_r][next_c]
                                union_cnt += 1

                    # while문이 끝나면 한 연합을 모두 찾은 것이므로 union list에 추가
                    union_list.append([union_sum, union_cnt])
        print(f'Day {answer}')
        for row in union_map:
            print(row)
        # 연합의 개수가 나라의 개수와 같다면 하나도 연합이 이뤄지지 않은 것
        if union_number == N * N - 1:
            break

        # 연합이 이뤄졌으므로 날짜를 하루 증가 시키고 인구 이동
        answer += 1
        for r in range(N):
            for c in range(N):
                union_sum, union_cnt = union_list[union_map[r][c]]
                map_[r][c] = union_sum // union_cnt
        print("map_")
        for row in map_:
            print(row)
        print("==========")
        
    print(answer)

# 22분 22초
# 백준 정답, 메모리 : 215908 KB, 시간 : 2600 ms
