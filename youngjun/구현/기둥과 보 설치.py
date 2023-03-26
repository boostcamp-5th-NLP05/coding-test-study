def solution(n, build_frame):
    answer = []
    #기둥조건1. 기둥은 바닥위
    #기둥조건2. 보의 한쪽 끝 부분 위 
    #기둥조건3. 다른 기둥위
    #보조건1. 한쪽 끝 부분이 기둥위
    #보조건2. 양쪽 끝 부분이 다른 보와 동시 연결
    #입력[c,r,기둥0 or 보1, 설치1 or 삭제0]
    map_ = [[[] for _ in range(n+2)]  for _ in range((n + 2))]
    
    for i in build_frame:
        if i[3] == 1: #설치 해야 될 때
            if i[2] == 0: #기둥일 때
                if i[1] == 0: #조건 1 바닥일 때
                    answer.append([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].append(0)
                    map_[i[1]+1][i[0]].append(0)
                    
                elif 0 in map_[i[1]][i[0]]: #조건 2 기둥 위일 때
                    answer.append([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].append(0)
                    map_[i[1]+1][i[0]].append(0)
                    
                elif 1 in map_[i[1]][i[0]]: #조건 3 보 위일 때
                    answer.append([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].append(0)
                    map_[i[1]+1][i[0]].append(0)
                else:
                    continue
            
            #보조건1. 한쪽 끝 부분이 기둥위
            #보조건2. 양쪽 끝 부분이 다른 보와 동시 연결
            if i[2] == 1: #보일 때
                if [i[0],i[1]-1,0] in answer or [i[0]+1,i[1]-1,0] in answer: #조건 1 기둥 위일 때
                    answer.append([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].append(1)
                    map_[i[1]][i[0]+1].append(1)
                    continue
                if [i[0]-1,i[1],1] in answer and [i[0]+1,i[1],1] in answer: #조건 2 양쪽 보일 때
                    answer.append([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].append(1)
                    map_[i[1]][i[0]+1].append(1)
                    continue
                
                continue
                    
        if i[3] == 0: #삭제 시
            if i[2] == 0: #기둥일 때
                if map_[i[1]][i[0]] == [0] and map_[i[1]+1][i[0]] == [0]: #주위에 아무것도 없을 때
                    answer.remove([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].remove(0)
                    map_[i[1]+1][i[0]].remove(0)
                    continue
                    
                if map_[i[1]+1][i[0]] == [0]: #조건 1 위에 보와 기둥 없을 시
                    answer.remove([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].remove(0)
                    map_[i[1]+1][i[0]].remove(0)
                    continue
                    
                if [i[0],i[1]+1,0] in answer and 1 not in map_[i[1]+1][i[0]]:
                    continue
                    
                if 1 in map_[i[1]+1][i[0]]:# and map_[i[1]+1][i[0]].count(0) < 2: #보만 있을 때
                    if map_[i[1]+1][i[0]].count(1) == 2: #양쪽으로 버틸 수 있을 때
                        answer.remove([i[0],i[1],i[2]])
                        map_[i[1]][i[0]].remove(0)
                        map_[i[1]+1][i[0]].remove(0)
                        continue
                        
                    if [i[0],i[1]+1,1] in answer:
                        if [i[0]+1,i[1],0] in answer:
                            answer.remove([i[0],i[1],i[2]])
                            map_[i[1]][i[0]].remove(0)
                            map_[i[1]+1][i[0]].remove(0)
                            continue

                    if [i[0]-1,i[1]+1,1] in answer:
                        if [i[0]-1,i[1],0] in answer:
                            answer.remove([i[0],i[1],i[2]])
                            map_[i[1]][i[0]].remove(0)
                            map_[i[1]+1][i[0]].remove(0)
                            continue
                    continue
                
                continue

            if i[2] == 1: #삭제할 것이 보일 때
                if map_[i[1]][i[0]+1] == [1] and map_[i[1]][i[0]].count(1) == 1: #보와 아무런 연결 없을 때
                    answer.remove([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].remove(1)
                    map_[i[1]][i[0]+1].remove(1)
                    continue
                
                if [i[0]-1,i[1],0] in answer and map_[i[1]][i[0]+1] == [1]:
                    answer.remove([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].remove(1)
                    map_[i[1]][i[0]+1].remove(1)
                    continue
                if [i[0]-1,i[1],0] in answer and [i[0]-1,i[1]+1,0] in answer:
                    answer.remove([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].remove(1)
                    map_[i[1]][i[0]+1].remove(1)
                    continue

                if [i[0]-1,i[1],0] in answer and [i[0]-1,i[1]+2,0] in answer:
                    answer.remove([i[0],i[1],i[2]])
                    map_[i[1]][i[0]].remove(1)
                    map_[i[1]][i[0]+1].remove(1)
                    continue

                continue
                            
    answer.sort(key = lambda x: (x[0],x[1],x[2]))
    return answer
