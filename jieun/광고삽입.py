import copy

class Time:
    def __init__(self, time_str=None, hr=0, mint=0, sec=0):
        if time_str:
            self.time_str = time_str
            self.h = int(time_str[:-6])
            self.m = int(time_str[-5:-3])
            self.s = int(time_str[-2:])
        else:
            self.h = int(hr)
            self.m = int(mint)
            self.s = int(sec)
            self.time_str = f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
            

    def __str__(self):
        return self.time_str

    def __add__(self, other):
        sec = self.s + other.s
        c = sec / 60
        sec %= 60
        mint = self.m + other.m + c
        c = mint / 60
        mint %= 60
        hr = self.h + other.h + c

        return Time(hr=hr, mint=mint, sec=sec)
    
    def __sub__(self, other):
        sec = self.s - other.s
        c = 0
        if sec < 0:
            sec += 60
            c = -1
        mint = self.m - other.m + c
        c = 0
        if mint < 0:
            mint += 60
            c = -1
        hr = self.h - other.h + c
        return Time(hr=hr, mint=mint, sec=sec)
        
    def __ge__(self, other):
        return  (self.h, self.m, self.s) >= (other.h, other.m, other.s)
    
    def __gt__(self, other):
        return (self.h, self.m, self.s) > (other.h, other.m, other.s)


def solution(play_time, adv_time, logs):
    answer = Time("00:00:00")
    answer_len = Time("00:00:00")
    play_time = Time(play_time)
    adv_time = Time(adv_time)
    
    time_logs = []
    for log in logs:
        tmp = log.split('-')
        time_logs.append((Time(tmp[0]), Time(tmp[1])))
    
    time_logs.sort()
    
    start = Time("00:00:00")
    dt = Time(sec = 1)
    
    while start < Time("100:00:00"):
        # print(start)
        end = start + adv_time
        res = Time("00:00:00")
        
        for idx, (s, e) in enumerate(time_logs):
            if e <= start: continue
            if s >= end: break
            
            t = min(end, e) - max(start, s)
            res += t
        
        
        if res > answer_len: 
            print(f"[{start},{end}] {res} {answer_len}")
            answer_len = copy.copy(res)
            answer = copy.copy(start)
        start += dt
       
    return answer.time_str

if __name__ == "__main__":
    # play_time = "02:03:55"
    # adv_time = "00:14:15"
    # logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    # result = "01:30:59"
    
    play_time = "99:59:59"
    adv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    result = "01:00:00"
    
    my_res = solution(play_time, adv_time, logs)
    
    print(my_res, (result == my_res))
