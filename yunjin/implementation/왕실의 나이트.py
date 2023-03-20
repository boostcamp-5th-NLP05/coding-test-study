import sys
from string import ascii_lowercase

input = sys.stdin.readline
position = input()
answer = 0

col, row = position[0], int(position[1])

# 영어 소문자 숫자로 바꾸기
col = ascii_lowercase.index(col) + 1

# 이동할 수 있는 경우
move_col = [2, 2, -2, -2, 1, -1, 1, -1]
move_row = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(8):
    ncol = col + move_col[i]
    nrow = row + move_row[i]

    # 밖으로 나가는 경우
    if ncol < 1 or ncol > 8 or nrow < 1 or nrow > 8:
        continue

    answer += 1

print(answer)