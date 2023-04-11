T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    dp = [[0 for _ in range(M)] for _ in range(N)]

    # dp 테이블을 금광으로 초기화
    for idx, val in enumerate(data):
        dp[idx // M][idx % M] = val
        # dp[r][c] = data[idx], idx = r*M + c

    for c in range(1, M):
        for r in range(N):
            x = dp[r][c - 1]  # 왼쪽에서부터 오는 경우
            if r > 0:
                x = max(x, dp[r - 1][c - 1])  # 왼쪽 위에서 온 경우
            if r + 1 < N:
                x = max(x, dp[r + 1][c - 1])  # 왼쪽 아래에서 온 경우
            dp[r][c] += x

    ans = max([dp[r][M - 1] for r in range(N)])  # 마지막 열 중 최대값
    print(ans)
