n = int(input())
data = []
for _ in range(n):
        name, score1, score2, score3 = map(str,input().split())
        data.append([name,int(score1),int(score2),int(score3)])
data.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

for i in data:
    print(i[0])