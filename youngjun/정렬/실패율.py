def solution(N, stages):
    answer = []
    stage_count = []
    player = len(stages)

    for i in range(1,N+1):
        if player == 0: #남은 사람이 없을 때 남아있는 스테이지 실패율 0으로
            for j in range(i,N+1):
                stage_count.append([j,0])
            break
            
        else: #[해당 스테이지,실패율] append
            stage_count.append([i,stages.count(i)/player])
            player -= stages.count(i)
        
    stage_count.sort(key = lambda x :(-x[1],x[0])) #실패율, 스테이지 순으로 정렬
    
    for i,_ in stage_count:
        answer.append(i)
    
    return answer