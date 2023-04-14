N, M = map(int, input().split())
arr = list(map(int, input().split()))

def to_give(h):
    # 절단기에 설정한 높이가 h일 때 잘린 떡의 길이 합
    cnt = 0
    for a in arr:
        if a > h:
            cnt += a - h
    return cnt

lo = 0
hi = max(arr) + 1
while lo+1 < hi:
    mid = (lo+hi)//2
    if to_give(mid) >= M: lo = mid
    else: hi = mid
    
print(lo)
    