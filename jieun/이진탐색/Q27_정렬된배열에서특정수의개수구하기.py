import bisect

N, x = map(int, input().split())
arr = list(map(int, input().split())) # 오름차순 정렬

upper_bound = bisect.bisect_right(arr, x) # 마지막 x의 오른쪽에 넣는 인덱스
lower_bound = bisect.bisect_left(arr,x) # 첫 번째 x의 왼쪽에 넣는 인덱스

ans = upper_bound - lower_bound
if ans == 0: print(-1)
else: print(ans)