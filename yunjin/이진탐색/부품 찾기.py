import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(input())
partials = list(map(int, input().split()))
M = int(input())
purchases = list(map(int, input().split()))

partials.sort()

answer = 0
for purchase in purchases:
    if binary_search(partials, purchase, 0, N-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')