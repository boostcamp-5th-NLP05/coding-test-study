if __name__ == "__main__":
    string = input()

    # 알파벳만 담은 배열 생성 -> 정렬 -> 다시 문자열 생성
    chars = [c for c in string if c.isalpha()]
    chars.sort()
    char_string = "".join(chars)

    # 정수만 담은 배열 생성. 생성 과정에서 int로 캐스팅 후 바로 합 구하기
    nums = sum([int(c) for c in string if c.isdigit()])

    # 답변 문자열 생성
    answer = f"{char_string}{nums}"
    print(answer)

    # 6분 33초
