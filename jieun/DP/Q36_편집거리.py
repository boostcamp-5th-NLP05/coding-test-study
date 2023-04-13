A = input()
B = input()
A_len = len(A)
B_len = len(B)

dp = [[0 for _ in range(B_len + 1)] for _ in range(A_len + 1)]
# 세로 A, 가로 B + 패딩
# dp[a][b] = A의 a번째 문자, B의 b번째 문자까지 비교했을 때 일치하는 가장 긴 부분문자열 길이

for a in range(1, A_len + 1):
    for b in range(1, B_len + 1):
        dp[a][b] = max(dp[a - 1][b], dp[a][b - 1])
        if A[a - 1] == B[b - 1]:
            dp[a][b] = max(dp[a][b], dp[a - 1][b - 1] + 1)

# same[b] = a (B의 b번째 문자와 A의 a번째 문자가 일치)
# same[b] = -1 이면 A 문자와 일치하지 않음
same = [-1 for _ in range(B_len)]

# dp 채운 경로 백트래킹
pa = A_len
pb = B_len
while pa > 0 and pb > 0:
    if A[pa - 1] == B[pb - 1]:
        same[pb - 1] = pa - 1
        pa -= 1
        pb -= 1
    elif dp[pa - 1][pb] > dp[pa][pb - 1]:
        pa -= 1
    else:
        pb -= 1

# (1) A와 일치하지 않은 B 문자는 삭제/교체
# (2) B와 일치하지 않은 A 문자 중 뒷 부분 삭제
ans = same.count(-1) + (A_len - max(same) - 1)

# (3) B와 일치하지 않은 A 문자 중 앞 부분 삭제
for i in same:
    if i > -1:
        ans += i
        break
print(ans)

# print(f"same:{same}")
# print("   " + "  ".join(B))
# for i in range(A_len):
#     print(A[i], end=" ")
#     print(dp[i+1][1:])
