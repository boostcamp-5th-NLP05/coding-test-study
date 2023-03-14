import sys
def gl():
    return sys.stdin.readline().rstrip()

S = gl()

ans = int(S[0]) # 첫 번째 자리 저장

# ans + S[i], ans * S[i] 중 큰 경우를 고른다.
for i in range(1, len(S)):
    n = int(S[i])
    if ans == 0 or n==0 or ans == 1 or n == 1:
        ans += n
    else: ans *= n
    
print(ans)
    