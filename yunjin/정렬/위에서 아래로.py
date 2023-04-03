import sys

input = sys.stdin.readline

N = int(input())
numbers = []

for i in range(N):
    numbers.append(int(input()))

numbers.sort(reverse=True)

for number in numbers:
    print(number, end=' ')
