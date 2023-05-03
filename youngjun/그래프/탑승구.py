#import sys

#def input():
#    return sys.stdin.readline().rstrip()

g = int(input())
p = int(input())

air = []
for i in range(p): 
    air.append(int(input()))

def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
    
parent = [i for i in range(g+1)] 
port = [0 for _ in range(g+1)] #탑승구에 들어와있는 지 보는 리스트
answer = 0

for i in air:
    tmp = find(parent,i) #현재 들어갈 수 있는 제일 번호가 큰 탑승구
    port[tmp] += 1
    if port[tmp] == 2: #두 대 들어왔으면 바로 break
        break
    answer += 1
    if tmp != 1:
        union(parent,tmp,tmp-1) #현재 도킹한 탑승구와 -1 번이랑 union

print(answer)