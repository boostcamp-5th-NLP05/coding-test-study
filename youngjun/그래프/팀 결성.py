n,m = map(int,input().split())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [i for i in range(n+1)] 
answer = []
for _ in range(m):
    tmp, a, b = map(int,input().split())
    if tmp == 0:
        union_parent(parent,a,b)
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            answer.append('YES')
        else:
            answer.append('NO')
            
for i in answer:
    print(i)
