N = int(input())

INF = 9876543210
prime = [2, 3, 5]

dp = [1, 2, 3, 4, 5]

for i in range(5, N):
    # 현재 len(dp) = i
    temp = INF
    for j in range(i - 1, -1, -1):
        for p in prime:  # [2,3,5]
            nxt = dp[j] * p
            if nxt > dp[i - 1]:  # dp[i-1]보다 큰 값 중 최소값 구해야 하므로 그 뒤는 안 봐도 됨.
                temp = min(temp, nxt)
                break
        if nxt <= dp[i - 1]:  # nxt = dp[j]*5
            break  # 다음에 볼 j는 현재보다 더 작으므로 안 봐도 됨.

    dp.append(temp)

print(dp[N - 1])
