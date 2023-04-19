N = int(input())
arr = list(map(int, input().split())) # 오름차순 정렬

lo = -1
hi = N-1
while lo+1<hi:
    mid = (lo+hi)//2

    # FFFTTT
    if arr[mid] >= mid: hi = mid
    else: lo = mid
    
if arr[hi] == hi: print(hi)
else: print(-1)

print(f"arr[{lo}] = {arr[lo]}")
