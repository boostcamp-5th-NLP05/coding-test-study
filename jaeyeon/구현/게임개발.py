if __name__=='__main__':
    N, M = map(int, input().split())
    cur_row, cur_col, cur_dir = map(int, input().split())

    # 0 : 육지, 1 : 바다
    game_map = []
    for _ in range(N):
        new_row = list(map(int, input().split()))
        game_map.append(new_row)

    # 0 : North, 1 : East, 2 : South, 3 : West
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    answer = 1                                  # 시작점도 방문 횟수에 포함
    while True:
        game_map[cur_row][cur_col] = 1          # 한 번 방문한 지점은 방문 못하기 때문에 바다로 만들어 버린다
        turn_cnt = 0
        while turn_cnt <= 4:                    # 4번 돌면 뒤로 가야하기 때문에 반복문 사용
            turn_cnt += 1
            cur_dir = (cur_dir + 3) % 4         # 반시계 방향이기 때문에 cur_dir - 1이 아닌 + 3
            next_row = cur_row + dr[cur_dir]
            next_col = cur_col + dc[cur_dir]

            # 다음으로 갈 지점이 조건에 부합한 지 확인. 부합하지 않으면 다음 회전으로 넘어가기
            if next_row < 0 or next_row > 7 or next_col < 0 or next_col > 7:
                continue
            
            if game_map[next_row][next_col] == 1:
                continue

            # 여기까지 실행이 됐다는건 조건에 부합하다는 것. 현재 위치 업데이트하고 turn_cnt 반복문 종료
            cur_row = next_row
            cur_col = next_col
            answer += 1
            break
        
        # 4번 회전했을 때 실행되는 부분
        if turn_cnt == 5:
            next_row = cur_row - dr[cur_dir]
            next_col = cur_col - dc[cur_dir]

            # 뒤로 가는 지점이 조건에 부합한지 확인
            if next_row < 0 or next_row > 7 or next_col < 0 or next_col > 7:
                break

            if game_map[next_row][next_col] == 1:
                break

            # 여기까지 실행 됐다는건 조건에 부합하다는 것. 뒤로 한 칸 가고 다시 1단계부터 시작
            cur_row = next_row
            cur_col = next_col

    print(answer)


# 24분 26초