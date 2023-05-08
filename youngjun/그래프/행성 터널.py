#import sys
#
#def input():
#    return sys.stdin.readline().rstrip()

def cost(a,b):
    cost_x = abs(a[0]-b[0])
    cost_y = abs(a[1]-b[1])
    cost_z = abs(a[2]-b[2])
    return min(cost_x,cost_y,cost_z)

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

n = int(input())
parent = [i for i in range(n)] 
edges = []
locs = []
#test = [[11, -15, -15], [14, -5, -15], [-1, -1, -5], [10, -4, -1], [19, -4, 19]]
for i in range(n):
    a = list(map(int, input().split()))
    #a = test[i]
    
    locs.append(a)
    
    for b in range(len(locs)): #이전 행성들과 거리 구하고 간선으로 추가
        edges.append((cost(a,gan[b]),i,b))

edges.sort() #간선은 총 comb(n,2)개

answer = 0
for edge in edges: #크루스칼 알고리즘
    cost, a, b = edge
    if  find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost

print(answer)