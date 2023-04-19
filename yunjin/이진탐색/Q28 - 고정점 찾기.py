import sys

input = sys.stdin.readline


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 오름차순이므로 인덱스와 비교해서 탐색
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

    return -1


N = int(input())
numbers = list(map(int, input().split()))

print(binary_search(numbers, 0, N - 1))
