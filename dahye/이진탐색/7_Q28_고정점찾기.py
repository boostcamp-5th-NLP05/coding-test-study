def binary_search(data, start, end): 
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == mid: # mid와 인덱스가 같으면 고정점
            return mid
        elif data[mid] > mid: # mid와 인덱스가 같은지 이진 탐색
            end = mid - 1
        else:
            start = mid + 1
    return -1

N= int(input())
data = list(map(int, input().split()))

data.sort()

print(binary_search(data, 0, N-1))