def solution(n, weak, dist):
    answer = []
    
    #각 지점 사이의 거리 구하기
    distance = []
    for i in range(len(weak)-1):  
        distance.append(weak[i+1] - weak[i])
    distance.append(n+weak[0] - weak[-1]) 
    
    dist.sort(reverse = True)
    
    #거리가 먼 곳을 지워가며 각 경우마다 최솟값을 answer에 저장 
    for i in range(1,len(distance)+1):

        idx = distance.index(max(distance))
        distance[idx] = 0
        for j in range(i,len(dist)):
            if sum(distance) <= sum(dist[:j]):
                answer.append(j)
                break
                
    if len(answer) == 0: #경우가 없다면 -1 반환
        return -1
    
    return min(answer) #최솟값 반환