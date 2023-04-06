import heapq

N = int(input())
data = []

for i in range(N):
    data.append(int(input()))
data.sort() 
heapq.heapify(data) #heap자료형으로 바꿈

answer = 0
while len(data) != 1:
    a = heapq.heappop(data)             #최솟값 두개 뽑기
    b = heapq.heappop(data)             

    answer += a
    answer += b

    heapq.heappush(data,a+b)            #합친 묶음 다시 넣어주기

print(answer)





