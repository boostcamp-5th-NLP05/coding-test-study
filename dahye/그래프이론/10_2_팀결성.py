# 두 학생이 속한 팀 찾기
def find_parent(parent,x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 학생이 속한 팀 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N,M = map(int,input().split())
parent = [0] * (N+1) # 팀 테이블 초기화

# 팀 테이블상에서 팀을 자기 자신으로 초기화
for i in range(1,N+1):
    parent[i] = i

answer = []

# union연산을 각각 수행
for i in range(M):
    m, a, b = map(int,input().split())
    if m == 0: # 팀 합치기일 때
        union_parent(parent,a,b)
    else: # 같은 팀 여부 확인
        if find_parent(parent,a) == find_parent(parent,b):
            answer.append('YES')
        else:
            answer.append('NO')

for ans in answer:
    print(ans)