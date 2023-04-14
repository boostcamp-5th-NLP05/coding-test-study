
import heapq
n = int(input())

factor = [2, 3, 5]
d = set([1,2,3,5]) # 못생긴 수 저장공간 2*5 & 5*2 등 곂칠 수 있으므로 set으로 정의
temp = [1,2,3,5] # 못생긴 수를 작은 수부터 뽑기 위한 임의 heap
heapq.heapify(temp) #heap자료형으로 바꿈

while len(temp) != 0 : #temp가 비어있으면 pop할 수 없음
    a = heapq.heappop(temp) #최소값 뽑기
    if a > 1000: #못생긴 수의 최솟값은 1000이므로
        break
    d.add(a)
    for i in factor:
        heapq.heappush(temp,a*i) # temp에 2,3,5를 곱한 값 넣어줌
#이후 실행에서 temp에 있는 값보다 작은 수가 나올 수 있으므로 계속 진행
d = sorted(d)

print(d[n-1]) #n번째 못생긴 수 print



