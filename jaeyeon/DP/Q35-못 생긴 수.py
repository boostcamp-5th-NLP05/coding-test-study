import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())

    # n의 범위에 따라 일찍 끝나는 조건 추가
    if n <= 6:
        print(n)
        exit()

    numbers = [1, 2, 3, 4, 5]
    dp = [False] * 100000000
    dp[1] = True
    dp[2] = True
    dp[3] = True
    dp[4] = True
    dp[5] = True
    dp[6] = True

    nums_cnt = 6
    last = 0
    idx = 7
    factors = [2, 3, 5]

    # 못 생긴 수 구하기
    while nums_cnt < n:
        for factor in factors:
            # 2 또는 3 또는 5로 나눈 수가 못 생긴 수라면 현재 수 또한 못 생긴 수
            if idx % factor == 0:
                if dp[idx // factor]:
                    last = idx
                    nums_cnt += 1
                    dp[idx] = True
                    break
        idx += 1

    # 마지막으로 업데이트 된 수 출력
    print(last)
