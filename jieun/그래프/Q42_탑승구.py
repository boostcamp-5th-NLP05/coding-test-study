# 백준 10775 정답: 37176 KB, 168 ms
import sys
import bisect
G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

parent = [i for i in range(G+1)] # parent[x]: x 번 이하 도킹할 수 있는 최대 탑승구


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    # 번호가 작은 집합에 합치기
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

ans = 0
break_flag = False

for _ in range(P):
    g = int(sys.stdin.readline().rstrip())
    if break_flag:
        continue
    
    y = find_parent(g) # y에 탑승
    if y == 0:
        break_flag = True
        continue
    
    union_parent(y, y-1) # y 이하 가능 탑승구 = y-1 이하 가능 탑승구
    ans += 1
    
print(ans)


# 시간 초과

# gates = [i for i in range(1, G+1)]
# ans = 0
# break_flag = False

# for _ in range(P):
#     g = int(sys.stdin.readline().rstrip())
#     if break_flag:
#         continue
    
#     # upper_bound
#     idx = bisect.bisect(gates, g)
#     if idx==0: 
#         break_flag = True
#         continue
    
#     del gates[idx-1]
#     ans += 1
    
# print(ans)
    
    
