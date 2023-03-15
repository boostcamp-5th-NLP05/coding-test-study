import sys


def gl():
    return sys.stdin.readline().rstrip()


N = int(gl())
arr = list(map(int, gl().split()))

arr.sort()

ans = 0
cnt = 0  # 현재 보는 그룹에 속한 인원

# 공포도가 작은 모험가부터 그룹화한다.
for x in arr:
    cnt += 1
    if cnt == x:  # x는 현재 보는 그룹 중 가장 큰 공포도
        ans += 1
        cnt = 0

print(ans)
