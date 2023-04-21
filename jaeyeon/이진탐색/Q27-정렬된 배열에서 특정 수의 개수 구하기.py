import sys
from bisect import bisect_left, bisect_right


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N, x = map(int, input().split())
    items = list(map(int, input().split()))

    # Lower bound 구하기
    start = bisect_left(items, x)

    # Upper bound 구하기
    end = bisect_right(items, x)

    answer = end - start
    if answer == 0: answer = -1
    print(answer)
