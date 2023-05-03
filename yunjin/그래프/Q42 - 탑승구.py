# 통과 풀이
import sys

input = sys.stdin.readline
G = int(input())
P = int(input())

numbers = []
for i in range(P):
    numbers.append(int(input()))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (G + 1)
for i in range(0, G + 1):
    parent[i] = i

answer = 0

for i in range(P):
    input_number = find_parent(parent, numbers[i])

    if input_number == 0: # union 전에 이미 루트가 0 이었다면 꽉 차서 못 넣으므로 종료.
        break

    union_parent(parent, input_number, input_number - 1) # 1 작은 수와 union
    answer += 1

print(answer)