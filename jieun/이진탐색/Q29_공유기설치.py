import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
house = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
house.sort()  # 집 위치 오름차순 정렬


def check(d):
    # 인접한 두 공유기의 거리가 최소 d일 수 있으면 True

    cnt = 1  # 0번째 집에 설치해서 1부터 시작
    s = 0  # 설치된 집
    e = 1  # 설치할 수 있을 지 보는 집

    while e < N and cnt < C:
        # 거리가 d 이상인 집에 설치
        if house[e] - house[s] >= d:
            cnt += 1
            s = e
        e += 1
    return cnt == C


# TTTFFF로 이분됨.
lo = 1
hi = house[N - 1] + 1  # 집 위치가 0부터 시작하므로

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)
