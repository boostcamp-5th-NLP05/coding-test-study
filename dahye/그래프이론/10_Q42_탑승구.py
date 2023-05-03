import sys

def input():
    return sys.stdin.readline().rstrip()

# 도킹한 비행기 존재 여부
def find_parent(parent,x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 도킹 가능하면 합침
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

G = int(input())
P = int(input())
parent = [0] * (G+1)

# 부모노드를 자기 자신으로 초기화
for i in range(1,G+1):
    parent[i] = i

count = 0
# 연결된 길에 대하여union연산을 각각 수행
for i in range(P):
    temp = find_parent(parent,int(input()))
    if temp == 0 : #도킹 불가능
        break
    union_parent(parent,temp-1,temp)

    count += 1
print(count)