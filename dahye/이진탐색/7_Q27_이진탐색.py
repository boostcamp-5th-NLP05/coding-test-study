def binary_search(data, x, start, end):
    global count
    if start < end:
        mid = (start + end) // 2
        if data[mid] == x: #mid를 기준으로 양옆에 모두 x가 존재 가능하므로
            count += 1
            binary_search(data, x, mid + 1, end) #재귀를 통해 x가 존재하면 전역변수인 count에 1씩더하는 구조
            binary_search(data, x, start, mid - 1)
        elif data[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    
    return count

N, x = map(int,input().split())
data = list(map(int, input().split()))

data.sort()

count = 0

if binary_search(data,x,0,N-1) == 0:
    print(-1)
else:
    print(binary_search(data, x, 0, N-1))
