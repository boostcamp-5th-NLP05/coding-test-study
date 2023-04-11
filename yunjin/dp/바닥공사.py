N = int(input())

dp = [0 for i in range(N + 1)]

dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 796796

print(dp[N])
