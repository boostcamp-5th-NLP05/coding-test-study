import heapq

def solution():
    n = int(input())
    heap = []
    for _ in range(n):
        heapq.heappush(heap,int(input()))   #힙큐에 입력
    
    answer = 0
    
    while len(heap) != 1:
        a = heapq.heappop(heap)             #최솟값 두개 뽑기
        b = heapq.heappop(heap)             
        
        answer += a
        answer += b
        
        heapq.heappush(heap,a+b)            #합친 묶음 다시 넣어주기

    print(answer)
    
solution()