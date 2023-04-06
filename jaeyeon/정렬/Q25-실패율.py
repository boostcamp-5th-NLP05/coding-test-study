import sys

def input():
    return sys.stdin.readline().rstrip()


def solution(N, stages):
    # 각 스테이지에 도달한 사용자 세기
    passed_users = [0 for _ in range(N)]
    for stage in stages:
        for i in range(min(stage, N)):
            passed_users[i] += 1

    fail_rates = []
    for idx, val in enumerate(passed_users):
        if val == 0:
            # 스테이지에 도달한 유저가 없는 경우이므로 해당 스테이지의 실패율은 0으로 정의
            fail_rates.append([0, idx + 1])
            continue
        
        # 해당 스테이지에 머물고 있는 사용자 수 세기
        cur = stages.count(idx + 1)
        
        # 실패율 계산하여 리스트에 추가하기
        fail_rates.append([cur / val, idx + 1])

    fail_rates.sort(key=lambda x: (-x[0], x[1]))
    answer = [idx for _, idx in fail_rates]
    return answer


if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))

# 프로그래머스 정답