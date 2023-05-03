#import sys

#def input():
#    return sys.stdin.readline().rstrip()

#n,m = map(int,input().split())
n = int(input())
m = int(input())

def find(parent,x):
    if parent[x] != x:
        x = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
    
parent = [i for i in range(n+1)]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1: #(i,j)가 1이면 간선처리
            union(parent,i+1,j+1)

travel = list(map(int,input().split()))

last = find(parent,travel[0])
for i in range(1,len(travel)):
    if find(parent,travel[i]) != last: #다른 union이면 NO 출력 및 break
        print("NO")
        break
    if i == len(travel) - 1: #마지막까지 돌았으면 YES 출력
        print("YES")