N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
height = numbers[0]

idx = 1
s = 0
answer = 0

def binary_search(start, end, numbers, M):
    result = 0
    while start <= end:
        mid = (start+end)//2

        s = 0
        for number in numbers:
            if number > mid:
                s += number - mid

        if s >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

print(binary_search(0, height, numbers, M))