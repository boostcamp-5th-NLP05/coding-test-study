import sys
from bisect import bisect_left, bisect_right


def input():
    return sys.stdin.readline().rstrip()

def binary_search(items, start, end):
    while start <= end:
        mid = (start + end) // 2
        if items[mid] == mid:
            return mid
        
        # 현재 보고 있는 인덱스에 해당하는 값이 인덱스보다 크다면 왼쪽편에 답이 있다는 뜻
        elif items[mid] > mid:
            end = mid - 1

        # 현재 보고 있는 인덱스에 해당하는 값이 인덱스보다 작다면 오른쪽편에 답이 있다는 뜻    
        else:
            start = mid + 1

    return -1

if __name__ == "__main__":
    N = int(input())
    items = list(map(int, input().split()))

    print(binary_search(items, 0, N-1))