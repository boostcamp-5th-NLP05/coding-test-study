def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    adv1,adv2,adv3 = map(int,adv_time.split(':'))
    adv_time = adv1*3600+adv2*60+adv3
    len_logs = len(logs)
    for i in range(len_logs) :
        a, b = logs[i].split('-')
        a1,a2,a3 = map(int,a.split(':')) #초단위로 계산
        b1,b2,b3 = map(int,b.split(':')) 
        logs[i] = [a1*3600+a2*60+a3, b1*3600+b2*60+b3]
    temp_cumul = 0
    logs.sort(key = lambda x:x[0]) #시청 시작구간을 기준으로 정렬
    for j in range(len_logs):
        cumul = 0
        start = logs[j][0] #공익광고 삽입 시간
        end = logs[j][0] + adv_time #공익광고 끝나는 시간

        for log_start, log_end in logs: #시청시간 안에 공익광고 시간만큼 누적값 더해줌
            if start <= log_start and end >= log_start:
                temp_st = log_start
                temp_ed = end
            elif start <= log_start and end >= log_end:
                temp_st = log_start
                temp_ed = log_end
            elif start <= log_end and end >= log_end:
                temp_st = start
                temp_ed = log_end
            elif start >= log_start and end <= log_end:
                temp_st = start
                temp_ed = end
            else:
                continue

            cumul += (temp_ed-temp_st) # 누적 재생시간 
        if cumul > temp_cumul: #현재 누적재생시간보다 크면 업데이트
            temp_cumul = cumul
            answer = start
    h = repr(answer//3600).zfill(2)
    m = str((answer%3600)//60).zfill(2)
    s = str((answer%3600)%60).zfill(2)

    return ':'.join([h,m,s])

print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))