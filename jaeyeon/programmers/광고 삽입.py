def time_to_second(time):
    play_h, play_m, play_s = map(int, time.split(":"))
    return play_h * 3600 + play_m * 60 + play_s


def second_to_time(second):
    h = second // 3600
    second %= 3600
    m = second // 60
    second %= 60
    s = second
    if h // 10 == 0:
        h = "0" + str(h)
    else:
        h = str(h)
    if m // 10 == 0:
        m = "0" + str(m)
    else:
        m = str(m)
    if s // 10 == 0:
        s = "0" + str(s)
    else:
        s = str(s)

    return f"{h}:{m}:{s}"


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    total_play_s = time_to_second(play_time)
    total_adv_s = time_to_second(adv_time)

    timeline = [0 for _ in range(total_play_s + 1)]
    for log in logs:
        start_time, end_time = log.split("-")
        start_s = time_to_second(start_time)
        end_s = time_to_second(end_time)
        timeline[start_s] += 1
        timeline[end_s] -= 1

    # 시간별 시청자 수 구하기
    for idx in range(1, total_play_s):
        timeline[idx] += timeline[idx - 1]

    # 시간별 누적 시청자 수 구하기
    for idx in range(1, total_play_s):
        timeline[idx] += timeline[idx - 1]

    # 광고 시작을 0초로 했을 때의 누적 시청시간을 초기값으로 설정
    max_val = timeline[total_adv_s - 1]
    max_idx = 0
    for i in range(total_adv_s, total_play_s):
        # timeline[time_a] - timeline[time_b] : time_a와 time_b 사이의 시청자 수(time_a > time_b)
        if max_val < timeline[i] - timeline[i - total_adv_s]:
            max_val = timeline[i] - timeline[i - total_adv_s]
            max_idx = i - total_adv_s + 1

    return second_to_time(max_idx)
