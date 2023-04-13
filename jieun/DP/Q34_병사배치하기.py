# 백준 18353 정답: 31256 KB, 688 ms
N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]
# dp[i]: i번 병사까지 배치할 때, 나열된 병사의 수
# i번 병사만 서 있는 경우로 초기화

for i in range(1, N):
    x = 0
    for j in range(i):
        # 앞에 있는 병사 중, i번 병사보다 전투력이 높은 병사만 고려
        if arr[j] > arr[i]:
            x = max(x, dp[j])

    dp[i] += x

ans = N - max(dp)
print(ans)
