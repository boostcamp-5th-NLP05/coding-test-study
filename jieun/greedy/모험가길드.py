import sys
def gl():
    return sys.stdin.readline().rstrip()

N = int(gl())
arr = list(map(int,gl().split()))

# 내림차순 정렬
arr.sort(reverse=True)

ans = 0
idx = 0 # 현재 보는 그룹 중 공포도가 가장 큰 모험가의 인덱스

# 공포도가 큰 모험가부터 그룹화한다.
while idx < N:
    ans += 1
    idx += arr[idx] # 그룹화 된 모험가 다음 인덱스

print(ans)
