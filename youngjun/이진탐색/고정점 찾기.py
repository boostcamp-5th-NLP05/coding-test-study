n = int(input())
nums = list(map(int,input().split()))

lo, hi = 0, n-1
answer = -1
while lo + 1 < hi:
    mid = (lo+hi) // 2
    if nums[mid] == mid:
        answer = mid
        break
    elif nums[mid] < mid:
        lo = mid
    else:
        hi = mid
print(answer)