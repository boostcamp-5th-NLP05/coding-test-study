import sys


def input():
    return sys.stdin.readline().rstrip()

        
if __name__ == "__main__":
    N = int(input())
    warriors = list(map(int, input().split()))
    in_list = [True] * N
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if warriors[j] > warriors[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(N - max(dp))

