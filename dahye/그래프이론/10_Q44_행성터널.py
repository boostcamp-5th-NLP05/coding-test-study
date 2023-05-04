import sys

def input():
    return sys.stdin.readline().rstrip()

# 특정원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(Union 연산)의 개수 입력 받기
N = int(input())
parent = [0] * (N) #부모 테이블 초기화하기

edges = [] # 모든 간선을 담을 리스트
loca = [] # 행성의 좌표를 담을 리스트 
result = 0 # 최종 비용을 담을 변수

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,N):
    parent[i] = i


# 행성의 좌표 입력받기
for _ in range(N):
    loca.append(list(map(int,input().split())))


#모든 간선에 대한 정보를 입력 받기
for n in range(N-1):
    for m in range(n+1,N):
        cost = min(abs(loca[n][0] - loca[m][0]),abs(loca[n][1] - loca[m][1]),abs(loca[n][2] - loca[m][2]))
        edges.append((cost,n,m)) #비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result) #최종 비용 출력