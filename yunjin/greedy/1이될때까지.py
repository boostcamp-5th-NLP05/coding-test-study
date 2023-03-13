N, K = map(int, input().split())

dp = [0 for i in range(N + 1)]
dp[1] = 1
if K == 2:
    dp[2] = 1
else:
    dp[2] = 2

dp[K] = 1

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + 1, dp[int(i/N)] + 1)

print(dp[N])
