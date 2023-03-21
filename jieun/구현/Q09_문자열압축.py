def solution(s):
    answer = len(s)

    # size는 문자를 압축시킬 단위
    for size in range(1, len(s)):
        result = ""  # 압축 문자열
        rep_str = s[:size]  # 반복하는지 확인하는 문자열. 앞 size 길이 문자열로 초기화.
        rep_cnt = 1  # rep_str가 반복되는 횟수

        # start는 볼 단위의 첫 번째 인덱스.
        for start in range(size, len(s), size):
            if rep_str == s[start : start + size]:
                # 앞 단위와 현재 보는 단위가 같다.
                rep_cnt += 1
            else:  # 다르다
                # 두 번 이상 반복하면 압축 문자열에 반복 횟수 추가
                if rep_cnt > 1:
                    result += str(rep_cnt)
                # 압축 문자열에 반복 문자열 추가
                result += rep_str
                # 반복 문자열과 반복 횟수를 초기화한다.
                rep_cnt = 1
                rep_str = s[start : start + size]
        # 마지막으로 저장되어 있는 반복 문자열을 압축 문자열에 추가
        if rep_cnt > 1:
            result += str(rep_cnt)
        result += rep_str
        rep_cnt = 1
        rep_str = s[start : start + size]
        # 답을 만든 압축 문자열과 비교해서 갱신
        answer = min(answer, len(result))

    return answer
