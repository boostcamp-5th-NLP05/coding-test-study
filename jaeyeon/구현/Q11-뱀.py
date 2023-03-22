if __name__ == "__main__":
    N = int(input())
    K = int(input())

    # 사과의 인덱스가 1부터 시작하므로 N+1 X N+1 짜리 보드 만들기
    board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    # 사과 추가
    for _ in range(K):
        r, c = map(int, input().split())
        board[r][c] = 1

    L = int(input())

    # 돌아야하는 시점 저장
    # 검색이 쉽도록 dict 형태로 저장
    turns = {}
    for _ in range(L):
        X, C = input().split()
        if C == "L":
            C = -1  # 반시계
        else:
            C = 1  # 시계
        turns[X] = C

    # 반시계 방향이 -1, 시계 방향이 1, 시작 방향이 오른쪽이므로 그에 맞게 dr, dc 설정
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 뱀 초기화
    snake = [[1, 1]]
    cur_dir = 0
    cur_r = 1
    cur_c = 1

    time = 0
    while True:
        time += 1

        # 다음 좌표 계산
        next_r = cur_r + dr[cur_dir]
        next_c = cur_c + dc[cur_dir]

        # 다음 좌표가 몸이랑 겹치면 멈추기
        if [next_r, next_c] in snake:
            break

        # 다음 좌표가 범위를 벗어나면 멈추기
        if next_r < 1 or next_r > N or next_c < 1 or next_c > N:
            break
        
        # 일단 몸을 늘려서 다음 칸에 위치
        snake.insert(0, [next_r, next_c])

        # 사과가 아니면 마지막 요소 삭제
        if board[next_r][next_c] != 1:
            snake.pop()

        # 사과면 요소 삭제는 생략하고 사과가 있는 칸을 0으로 만들기
        else:
            board[next_r][next_c] = 0

        # 현재 위치 업데이트
        cur_r = next_r
        cur_c = next_c

        # X초가 끝난 뒤에 방향을 바꾸므로 다음 반복문이 시작되기 전에 회전 여부 확인
        if str(time) in turns:
            cur_dir = (cur_dir + turns[str(time)]) % 4

    print(time)

# 백준 정답
# 23분 41초
