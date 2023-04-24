def find_w(query):
    if query[0] == "?":
        if query[-1] == "?":
            return [0, len(query)]

        start = 0
        end = len(query) - 1
        while start <= end:
            mid = (start + end) // 2
            if query[mid] == "?":
                start = mid + 1
            else:
                end = mid - 1
        return [0, start]
    else:
        start = 0
        end = len(query) - 1
        while start <= end:
            mid = (start + end) // 2
            if query[mid] == "?":
                end = mid - 1
            else:
                start = mid + 1
        return [start, len(query)]


def solution(words, queries):
    answer = []

    for query in queries:
        # 물음표의 시작과 끝 찾기
        start, end = find_w(query)  # query[start : end] 가 와일드카드
        count = 0
        comp_q = query[:start] + query[end:]

        # 물음표를 제외한 나머지 부분 비교
        for word in words:
            if len(word) < end:
                continue
            comp_w = word[:start] + word[end:]
            if comp_q == comp_w:
                count += 1

        answer.append(count)

    return answer


# 효율성 테스트 1,2,3 시간 초과
