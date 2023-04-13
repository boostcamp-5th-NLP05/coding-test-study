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
    # 얻을 수 있는 최대 이익
    max_val = 0

    # i일부터 마지막날까지 일했을 때의 최대 이익
    for i in range(N-1, -1, -1):
        if i + time[i] <= N: 
            dp[i] = max(dp[i + time[i]] + pay[i], max_val)
            max_val = dp[i]

        else:
            dp[i] = max_val
    
    print(max_val)
    