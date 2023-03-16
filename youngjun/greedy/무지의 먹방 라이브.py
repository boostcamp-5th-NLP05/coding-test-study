def solution():
    food_times = list(map(int, input().split()))
    k = int(input())
    
    if sum(food_times) <= k: #k이전에 음식을 다 먹은 경우
        return -1

    len_not_zero = len(food_times) #0이 아닌 개수 즉, 한 사이클 크기
    
    while k >= len_not_zero:
        
        a,b = divmod(k,len_not_zero) #사이클 횟수 + 남는 횟수
        
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] = food_times[i] - a #사이클 만큼 빼기
            else:
                continue

        cnt = 0
        minus = 0
        
        for i in range(len(food_times)):
            if food_times[i] <= 0:
                minus -= food_times[i] #마이너스 만큼 갱신된 k에 더하기
                food_times[i] = 0
            else:
                cnt +=1  #0 이 아닌 개수 갱신
                
        len_not_zero = cnt      
        k = minus + b #마이너스 + 원래 나머지를 더해서 k 갱신
        
    cnt = 0
    idx = 0
    
    #결국 한 사이클을 못돌리는 k가 남는다
    
    for i in range(len(food_times)):
        if food_times[i] > 0:
            cnt += 1

        if cnt == k+1: #k초 이후에 먹을 음식 인덱스
            idx = i
            break
    
    return idx +1

solution()