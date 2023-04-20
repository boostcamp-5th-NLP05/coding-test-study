def lower_bound(query: str, char_len: int, symb_len: int, words):
    q = query[:char_len]
    lo = -1
    hi = len(words)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        # mid >= target FFFTTT
        if words[mid][:char_len] > q or (
            words[mid][:char_len] == q and len(words[mid]) - char_len >= symb_len
        ):
            hi = mid
        else:
            lo = mid
    return hi


def upper_bound(query: str, char_len: int, symb_len: int, words):
    q = query[:char_len]
    lo = -1
    hi = len(words)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        # mid > target FFFTTT
        if words[mid][:char_len] > q or (
            words[mid][:char_len] == q and len(words[mid]) - char_len > symb_len
        ):
            hi = mid
        else:
            lo = mid
    return hi


def find_question(query: str):
    # aaa???
    lo = -1
    hi = len(query) - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        # is ?: FFFTTT
        if query[mid] == "?":
            hi = mid
        else:
            lo = mid
    return hi


def solution(words, queries):
    answer = []
    cnt = dict()

    backward_words = ["".join(reversed(w)) for w in words]
    backward_words.sort()
    words.sort()

    print("words:", words)
    print("backward_words:", backward_words)
    print("queries:", queries)

    for q in queries:
        if q[0] == "?":
            q = "".join(reversed(q))
            print(f"{''.join(reversed(q))} --> {q} :", end=" ")
            if q in cnt:
                answer.append(cnt[q])
            else:
                idx = find_question(q)
                u = upper_bound(q, idx, len(q) - idx, backward_words)
                l = lower_bound(q, idx, len(q) - idx, backward_words)
        else:
            print(q, ":", end=" ")
            if q in cnt:
                answer.append(cnt[q])
            else:
                idx = find_question(q)
                u = upper_bound(q, idx, len(q) - idx, words)
                l = lower_bound(q, idx, len(q) - idx, words)

        print(u, l)
        res = u - l
        cnt[q] = res
        answer.append(res)

    return answer


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    ans = [3, 2, 4, 1, 0]
    res = solution(words, queries)
    print(res, ans)
    print(res == ans)
