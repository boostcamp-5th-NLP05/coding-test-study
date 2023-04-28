# https://school.programmers.co.kr/learn/courses/30/lessons/72414

# 시간 문자열을 초로 변환
def str_to_sec(time_str):
    t = time_str.split(":")
    sec = int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])
    return sec


# 초를 시간 문자열로 변환
def sec_to_str(sec: int):
    hr = sec // 3600
    sec %= 3600
    mint = sec // 60
    sec %= 60
    return f"{hr:02d}:{mint:02d}:{sec:02d}"


def solution(play_time, adv_time, logs):
    play_sec = str_to_sec(play_time)
    adv_sec = str_to_sec(adv_time)

    # 광고 시간이 동영상 재생 시간 보다 길면 00:00:00 반환
    if adv_sec >= play_sec:
        return sec_to_str(0)

    # cnt[i]: 구간 [i, i+1) 의미
    cnt = [0 for _ in range(play_sec + 1)]
    for time_str in logs:
        start, end = time_str.split("-")
        start = str_to_sec(start)
        end = str_to_sec(end)
        cnt[start] += 1
        cnt[end] -= 1

    # cnt 누적합 구해서 각 구간마다 시청자 재생 횟수 구하기
    for i in range(play_sec):
        cnt[i + 1] += cnt[i]

    answer_start = 0
    answer_sec = sum(cnt[:adv_sec])  # 00:00:00에 광고를 삽입했을 때
    res = answer_sec

    for s in range(1, play_sec):
        if s + adv_sec > play_sec:
            break
        res = res - cnt[s - 1] + cnt[s + adv_sec - 1] # 맨 앞 1초 제거, 뒤에 새로운 1초 추가
        if res > answer_sec:
            answer_sec = res
            answer_start = s

    return sec_to_str(answer_start)
