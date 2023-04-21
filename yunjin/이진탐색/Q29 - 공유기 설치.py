import math, sys

input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for i in range(n)]
houses.sort()

# 집 사이의 최소 거리, 최대 거리
start, end = 1, houses[n - 1] - houses[0]

result = 0

if c == 2:

    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
    print(houses[n - 1] - houses[0])

else:

    # 이진 탐색
    while (start < end):
        mid = (start + end) // 2

        count = 1
        old = houses[0]

        # 마지막으로 설치된 공유기의 위치
        for i in range(n):
            if houses[i] - old >= mid:  # 공유기 거리가 mid 이상이면 설치함.
                count += 1
                old = houses[i] # 공유기 위치 갱신

        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(result)
