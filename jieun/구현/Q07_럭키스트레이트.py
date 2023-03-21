import sys

score = list(map(int, sys.stdin.readline().rstrip()))

half = int(len(score) / 2)  # 점수를 자릿수 기준 반으로 나누는 인덱스
left_sum = sum(score[:half]) # 왼쪽 부분의 각 자릿수 합
right_sum = sum(score[half:]) # 오른쪽 부분의 각 자릿수 합

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
