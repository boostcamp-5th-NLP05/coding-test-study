from collections import Counter


def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):

        count = stages.count(i)  # 사람 수 계싼

        # 실패율
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count  # 인구 업데이트

    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]

    return answer
