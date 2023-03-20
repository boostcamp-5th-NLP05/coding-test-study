pos = input()

r = int(pos[1]) - 1  # [0,7] 사이 숫자
c = ord(pos[0]) - ord("a")  # [0,7] 사이 숫자
# ord(char): 문자를 아스키코드값(int)로 변환

# 나이트가 갈 수 있는 경우의 좌표 변화율
dr = [-2, -2, -1, 1, 2, 2, -1, 1]
dc = [-1, 1, 2, 2, -1, 1, -2, -2]

ans = 0
for i, j in zip(dr, dc):
    nr = r + i
    nc = c + j
    # 갈 위치가 체스판 안인지 확인
    if 0 <= nr and nr < 8 and 0 <= nc and nc < 8:
        ans += 1

print(ans)
