N, M = map(int, input().split())
arr = map(int, input().split())

# cnt[x]: 무게 x인 공의 개수
cnt = [0 for _ in range(M + 1)]
for i in arr:
    cnt[i] += 1

ans = 0
for i in range(1, M):
    for j in range(i + 1, M + 1):
        # 무게 조합 (i,j)에 해당하는 번호 조합 개수를 구한다.
        ans += cnt[i] * cnt[j]

print(ans)
