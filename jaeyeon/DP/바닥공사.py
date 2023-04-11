import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())

    dp = [0] * 1001

    dp[1] = 1
    dp[2] = 3

    # 2 x 1 타일을 채우는 경우는 1개, 2 x 2 타일을 채우는 경우는 2개이므로 아래와 같이 식 구성
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796

    print(dp[N])
