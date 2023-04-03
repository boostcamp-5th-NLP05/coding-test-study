import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    nums.sort(reverse=True)
    print(nums)
