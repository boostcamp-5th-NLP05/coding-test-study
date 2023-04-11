N = int(input())
dp = []
# dp 테이블을 정수 삼각형 값으로 초기화
for _ in range(N):
    line = list(map(int, input().split()))
    dp.append(line)

for r in range(1, N):
    dp[r][0] += dp[r - 1][0]  # 첫 칸은 대각선 오른쪽 위에서밖에 못 옴
    dp[r][r] += dp[r - 1][r - 1]  # 마지막 칸은 대각선 왼쪽 위에서밖에 못 옴
    for c in range(1, r):
        x = dp[r - 1][c]  # 대각선 오른쪽 위에서 온 경우
        if c > 0:
            x = max(x, dp[r - 1][c - 1])  # 대각선 왼쪽 위에서 온 경우
        dp[r][c] += x

ans = max(dp[N - 1])  # 마지막 층에서 최대값
print(ans)
