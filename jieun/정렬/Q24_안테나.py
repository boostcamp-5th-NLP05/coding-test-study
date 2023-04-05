# 백준 18310 정답: 53144 KB, 268 ms, Python3
import sys

N = int(sys.stdin.readline().rstrip())
pos = list(map(int, sys.stdin.readline().rstrip().split()))

pos.sort()
# dist[i]: i번째와 i-1번째 집 사이 거리
dist = [0] + [pos[i] - pos[i - 1] for i in range(1, N)]

left = 0  # 왼쪽 거리 합
right = 0  # 오른쪽 거리 합

# 0번째 집에 위치했을 때 거리 총 합
for i in range(1, N):
    right += dist[i] * (N - i)

min_dist = right
ans = pos[0]

# i 번째 집에 위치할 때
for i in range(1, N):
    left += dist[i] * i # i번째 집에 대해 dist[i]가 반복될 값
    right -= dist[i] * (N - i) # (i-1)번 째 집에 대해 dist[i]가 반복된 값
    cur_dist = left + right
    if cur_dist < min_dist:
        min_dist = cur_dist
        ans = pos[i]

print(ans)
