from collections import Counter

N, M = map(int, input().split())
balls = list(map(int, input().split()))

answer = 0

l = len(balls)

# Counter를 이용해서 각 무게 별로 몇개가 있는지 확인.
x = sorted(Counter(balls).items())

# 전략 : 순서를 고려하고 서로 다른 무게를 고른다. -> 작은 무게 부터 전체 점검하되 같은 무게는 고려 대상에서 제외한다
# 조합될 수 있는 l 의 값을 점점 줄여 나간다. 동일 무게들을 점점 제거 해나간다.
for idx, value in x:

    # 동일 무게 제거
    # l 은 곱의 대상이 될 볼링볼 수
    l -= value

    # 고른 볼링공과 같은 무게인 볼링공은 서로 다르게 취급 된다. -> value 를 곱해줌
    answer += value * l

print(answer)
