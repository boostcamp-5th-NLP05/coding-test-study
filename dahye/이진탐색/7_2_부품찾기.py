import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
data1 = list(map(int,input().split()))
M = int(input())
check = list(map(int,input().split()))

for i in check: #확인요청한 부품이 list에 들어있는지 여부를 in으로 판별
    if i in data1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')