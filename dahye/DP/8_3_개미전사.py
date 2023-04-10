N = int(input())
data = list(map(int,input().split()))

d = [0] * 100 
d[0] = data[0]
d[1] = max(data[0],data[1]) #최소 한칸 이상 떨어진 식량창고를 약탈해야하므로 둘중 큰 값 할당

for i in range(2, N):
     d[i] = max(d[i - 1],d[i - 2]+data[i])

print(d[i])