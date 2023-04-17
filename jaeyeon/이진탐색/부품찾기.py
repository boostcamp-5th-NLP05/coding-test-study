import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def binary_search(items, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if items[mid] == target:
            return True
        elif items[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == "__main__":
    N = int(input())
    items = list(map(int, input().split()))
    M = int(input())
    requires = list(map(int, input().split()))

    items.sort()

    # 이진 탐색을 통해 손님이 요청한 부품이 있는지 찾기
    for require in requires:
        if binary_search(items, require, 0, N - 1):
            print("yes", end=" ")
        else:
            print("no", end=" ")
    print(" ")
