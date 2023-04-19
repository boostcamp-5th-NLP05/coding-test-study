n, x = map(int,input().split())
nums = list(map(int,input().split()))

temp = -1
lo, hi = 0, n-1

while lo + 1 < hi:
    mid = (lo+hi) // 2
    if nums[mid] == x:
        temp = mid
        break
    elif nums[mid] < x:
        lo = mid
    else:
        hi = mid

def find_under(lo,hi):
    while lo + 1 < hi:
        mid = (lo+hi) // 2
        if nums[mid] == x:
            hi = mid
        else:
            lo = mid
    return hi
        
def find_upper(lo,hi):
    while lo + 1 < hi:
        mid = (lo+hi) // 2
        if nums[mid] == x:
            lo = mid
        else:
            hi = mid
    return lo

        
if temp == -1:
    print(-1)
else:
    print(find_upper(temp,n) - find_under(0,temp) + 1)
    