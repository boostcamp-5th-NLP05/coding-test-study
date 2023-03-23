def solution(s):
    r = []

    # i 는 문자를 몇 개 단위로 자를지 여부
    for i in range(1, len(s) + 1):
        cnt = 1
        substring = s[:i]
        checkstring = ''

        # 문자열비교, i 단위로 움직인다.
        for j in range(i, len(s) + i, i):

            if substring == s[j:j + i]:
                cnt += 1

            # 같지 않은 경우에 초기화 시켜주고 다시 반복문 돈다.
            else:

                if cnt != 1:
                    checkstring += str(cnt) + substring
                else:
                    checkstring += substring
                cnt = 1
                substring = s[j:j + i]

        r.append(len(checkstring))

    answer = min(r)
    return answer