if __name__ == "__main__":
    position = input()
    col = ord(position[0]) - ord('a')
    row = int(position[1]) - 1
    
    cnt = 0
    # 반복문으로 다음 위치가 체스판 내에 있는지 확인
    for i in [-2,2]:
        for j in [-1, 1]:
            # 반복문은 4번만 돌리되, row와 col에 i와 j를 각각 더하며 한 반복문 당 포지션 2개 확인
            next_row = row + i
            next_col = col + j
            if 0 <= next_row <= 7 and 0 <= next_col <= 7:
                cnt += 1

            next_row = row + j
            next_col = col + i
            if 0 <= next_row <= 7 and 0 <= next_col <= 7:
                cnt += 1

    print(cnt)

# 16분 30초