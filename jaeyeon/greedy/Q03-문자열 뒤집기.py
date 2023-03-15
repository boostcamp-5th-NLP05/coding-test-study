if __name__=="__main__":
    line = input()

    # 1을 기준으로 split하여 0으로만 이루어진 리스트 구하기
    line_zero = line.split("1")

    # 0을 기준으로 split하여 1로만 이루어진 리스트 구하기
    line_one = line.split("0")

    # 각각의 리스트에서 길이가 0인 요소를 제외하고 갯수 세기
    cnt_zero = len([tok for tok in line_zero if len(tok) != 0])
    cnt_one = len([tok for tok in line_one if len(tok) != 0])
    
    # 둘 중 더 작은 값을 answer로
    answer = min(cnt_zero, cnt_one)

    print(answer)