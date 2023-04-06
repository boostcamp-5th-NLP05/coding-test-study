N = int(input())
data = []
for i in range(N):
    temp = list(input().split())
    data.append([temp[0]] + list(map(int,temp[1:])))

data.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

for name in data:
    print(name[0])