import sys

def input():
    return sys.stdin.readline().rstrip()

# 도로 연결 여부
def find_parent(parent,x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 도로 연결하기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N,M = map(int,input().split())
parent = [0] * (N+1)

# 부모노드를 자기 자신으로 초기화
for i in range(1,N+1):
    parent[i] = i

answer = "YES"

# 연결된 길에 대하여union연산을 각각 수행
for i in range(N):
    data = list(map(int,input().split()))
    for j in range(i+1,N):
        if data[j] == 1: #합치기
            union_parent(parent,i,j)
# 도로로 연결되어있는지 확인하면서 여행 가능여부 체크

temp = list(map(int,input().split()))
for m in range(M-1):
    if find_parent(parent,temp[m]) != find_parent(parent,temp[m+1]): # 부모노드가 다르면 이동 불가
        answer = "NO"

print(answer)
