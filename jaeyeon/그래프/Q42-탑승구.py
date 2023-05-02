import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    G = int(input())
    P = int(input())

    gates = [int(input()) for _ in range(P)]

    gates.sort(key=lambda x: -x)

    answer = 1
    for idx in range(1, P):
        # 비행기들은 들어갈 수 있는 탑승구 중 번호가 가장 큰 탑승구에 도킹한다는 가정
        if gates[idx - 1] <= gates[idx]:
            # 이전 비행기보다는 작은 탑승구에 들어가야 한다.
            gates[idx] = gates[idx - 1] - 1

        # 값이 0이 되었다는 뜻은 갈 수 있는 탑승구가 모두 자리가 차버렸다는 뜻
        if gates[idx] != 0:
            answer = idx + 1
        else:
            break

    print(answer)
