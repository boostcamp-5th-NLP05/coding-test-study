import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())

    # 큰 수로 dp 배열 초기화
    INF = 987654321
    dp = [INF] * (N * 5)
    dp[1] = 0
    factors = [2, 3, 5]

    # num: 숫자, count: 그 번호까지 도달하기 위한 최소 연산 횟수
    for num, count in enumerate(dp):
        if num == N:
            break

        if num == 0:
            continue

        # 바텀업 방식으로 dp의 값들을 최소값으로 업데이트
        for factor in factors:
            dp[num * factor] = min(dp[num * factor], count + 1)

        dp[num + 1] = min(dp[num + 1], count + 1)

    print(dp[N])
