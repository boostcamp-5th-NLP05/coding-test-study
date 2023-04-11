import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())
    dp = []
    for _ in range(n):
        dp.append(list(map(int, input().split())))

    # 한 행씩 내려가며 업데이트
    for r in range(1, n):
        for c in range(len(dp[r])):
            if c == 0:
                dp[r][c] += dp[r - 1][c] # 바로 위 값 더하기

            elif c == len(dp[r]) - 1:
                dp[r][c] += dp[r - 1][c - 1] # 왼쪽 위 값 더하기

            else:
                dp[r][c] += max(dp[r - 1][c - 1], dp[r - 1][c])
                # 왼쪽 위 값, 바로 위 값 비교

    #마지막 줄의 최대값 출력
    print(max(dp[-1]))


# 7분 26초
# 백준 정답, 메모리 : 116200 KB, 시간 : 156 ms
