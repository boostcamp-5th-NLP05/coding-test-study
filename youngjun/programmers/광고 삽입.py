def solution(play_time, adv_time, logs):
    
    def to_sec(time):
        time_split = time.split(":")
        sec = (int(time_split[0]) * 3600) + (int(time_split[1])*60) + int(time_split[2])
        return sec
    
    play_time_sec = to_sec(play_time)
    adv_time_sec = to_sec(adv_time)
    logs_sec = []
    time_list = [0] * (play_time_sec)
    
    #time_list에 로그에 있는 만큼 더해주기
    for i in logs:
        a,b = i.split("-")
        a_sec = to_sec(a)
        b_sec = to_sec(b)
        logs_sec.append([a_sec,b_sec])
        for i in range(a_sec,b_sec):
            time_list[i] += 1

    total_time = sum(time_list[0:adv_time_sec])
    answer_sec = 0

    #로그 시작점,끝점에 맞춰서 리스트에서 광고 길이 만큼 리스트 합 구하기
    for start,end in logs_sec:
        if (start + adv_time_sec) <= play_time_sec:
            start_sum = sum(time_list[start:start+adv_time_sec])
            if total_time == start_sum:
                answer_sec = min(start,answer_sec)
            elif total_time < start_sum:
                answer_sec = start
                total_time = start_sum
        
        if (end - adv_time_sec) >= 0:
            end_sum = sum(time_list[end-adv_time_sec:end])
            if total_time == end_sum:
                answer_sec = min(answer_sec,end-adv_time_sec)
            elif total_time < end_sum:
                answer_sec = end-adv_time_sec
                total_time = end_sum
    
            
    #초 단위를 출력 형식으로 
    time = answer_sec
    a = time // 3600
    time -= a*3600 
    b = time // 60
    time -= b*60
    c = time
    
    a,b,c = str(a),str(b),str(c)
    
    if len(a) == 1:
        a = '0' + a
    if len(b) == 1:
        b = '0' + b
    if len(c) == 1:
        c = '0' + c

    answer = str(a) + ':' + str(b) + ':' + str(c)
    
    return answer