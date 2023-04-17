N = int(input())
arr = list(map(int, input().split()))
M = int(input())
to_find = list(map(int, input().split()))

arr.sort()

def is_in(target):
    # target이 arr 안에 있는지 이진 탐색
    lo = -1
    hi = N-1
    while lo+1 < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target: lo = mid
        else: hi = mid
    if arr[hi] == target: return True
    else: return False

ans = []
for target in to_find:
    if is_in(target):
        ans.append("yes")
    else:
        ans.append("no")
        
print(" ".join(ans))