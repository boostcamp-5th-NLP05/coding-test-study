def time_to_sec(time):
    a1,a2,a3 = map(int,time.split(':')) #초단위로 계산
    return a1*3600+a2*60+a3

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    adv1,adv2,adv3 = map(int,adv_time.split(':'))
    adv_time = adv1*3600+adv2*60+adv3
    time_list = [0] * time_to_sec(play_time)
    start_end = [] # 각 광고들의 처음과 끝

    for log in logs : # log들을 초단위로 변경
        a, b = log.split('-')
        start_end.append((time_to_sec(a), time_to_sec(b)))
        for i in range(time_to_sec(a),time_to_sec(b)): #해당 초에 보는 시청자수 구하기
            time_list[i] += 1

    temp = sum(time_list[0:adv_time])
    answer = 0

    for s,e in start_end: # 광고의 처음과 끝을 기준으로 시청자 수 count
        if (s + adv_time) <= time_to_sec(play_time):
            start_sum = sum(time_list[s:s+adv_time])
            if  temp == start_sum: # 같으면 먼저나온 광고
                answer = min(s,answer)
            elif  temp < start_sum:
                answer = s
                temp = start_sum

        if (e - adv_time) >= 0:
            end_sum = sum(time_list[e-adv_time:e])
            if  temp == end_sum: # 같으면 먼저나온 광고
                answer = min(e-adv_time,answer)
            elif  temp < end_sum:
                answer = e-adv_time
                temp = end_sum


    h = repr(answer//3600).zfill(2)
    m = str((answer%3600)//60).zfill(2)
    s = str((answer%3600)%60).zfill(2)

    return ':'.join([h,m,s])

print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))