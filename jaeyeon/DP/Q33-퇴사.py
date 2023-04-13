import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    time, pay = [], []
    for _ in range(N):
        t, p = list(map(int, input().split()))
        time.append(t)
        pay.append(p)

    dp = [0] * (N+1)
    max_val = 0
    for i in range(N-1, -1, -1):
        if i + time[i] <= N: 
            dp[i] = max(dp[i + time[i]] + pay[i], max_val)
            max_val = dp[i]

        else:
            dp[i] = max_val
    
    print(dp[0])
    