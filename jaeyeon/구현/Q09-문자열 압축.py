def solution(s):
    N = len(s)

    # 길이가 1일 경우 9번줄이 실행되지 않으므로 1 반환
    if N == 1:
        return 1
    
    answer = 1000
    for slice in range(1, N // 2 + 1):              # N 길이의 반까지만 확인
        new_string = ""
        string_copy = s
        while len(string_copy) >= slice:            # string_copy에서 sub를 계속 빼줌
            sub = string_copy[:slice]
            remain = string_copy[slice:]
            string_copy = remain
            cnt = 1
            while sub == string_copy[:slice]:       # sub와 같은 sub string이 있으면 카운트하고
                cnt += 1                            
                string_copy = string_copy[slice:]   # 문자열에서 제거

            if cnt >= 2:                            # 같은 sub가 하나 밖에 없으면 그냥 두는게 낫다
                new_string += f"{cnt}{sub}"
            else:
                new_string += sub
        if len(string_copy) != 0:                   # 남은 string 추가
            new_string += string_copy

        answer = min(answer, len(new_string))
    return answer


if __name__ == "__main__":
    s = input()
    print(solution(s))

# 25분 37초
# 정확성 100점
