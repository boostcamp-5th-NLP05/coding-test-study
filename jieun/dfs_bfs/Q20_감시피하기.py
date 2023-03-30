# 백준 18428 제출: 39836 KB, 216 ms, Python3
import sys
import itertools

N = int(sys.stdin.readline().rstrip())
map_ = []
for _ in range(N):
    map_.append(sys.stdin.readline().rstrip().split())

empty = [(r, c) for r in range(N) for c in range(N) if map_[r][c] == "X"]  # 빈 칸
student = [(r, c) for r in range(N) for c in range(N) if map_[r][c] == "S"]  # 학생 칸

# (r,c)에 있는 학생이 감시를 피할 수 있는지 반환
def is_hidden(r, c):
    up = r - 1
    down = r + 1
    left = c - 1
    right = c + 1
    
    while up >= 0:  # 위 방향을 본다.
        if map_[up][c] == "O":
            break
        if map_[up][c] == "T":
            return False
        up -= 1
        
    while down < N:  # 아래 방향을 본다.
        if map_[down][c] == "O":
            break
        if map_[down][c] == "T":
            return False
        down += 1
        
    while left >= 0:  # 왼쪽 방향을 본다.
        if map_[r][left] == "O":
            break
        if map_[r][left] == "T":
            return False
        left -= 1
        
    while right < N:  # 오른쪽 방향을 본다.
        if map_[r][right] == "O":
            break
        if map_[r][right] == "T":
            return False
        right += 1
    return True


for case in itertools.combinations(empty, 3):  # 빈 칸 3개를 고른다.
    for r, c in case:  # 고른 빈 칸을 장애물이라고 표시
        map_[r][c] = "O"

    all_hidden = True  # 모든 학생이 감시를 피할 수 있는지 여부
    for r, c in student:
        if not is_hidden(r, c):  # 학생 중 한 명이라도 감시에 걸리면 for문 탈출
            all_hidden = False
            break

    if all_hidden:
        break

    for r, c in case:  # 장애물 칸 빈 칸으로 원상복귀
        map_[r][c] = "X"

if all_hidden:
    print("YES")
else:
    print("NO")
