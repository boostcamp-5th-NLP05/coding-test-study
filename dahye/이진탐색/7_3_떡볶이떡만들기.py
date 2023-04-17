import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
data = list(map(int,input().split()))

count = 0 #현재 떡 개수
temp = max(data) #절단기 높이
while M > count :
    count = 0
    for i in data:
        if i - temp > 0 :
            count += (i-temp)

    temp -= 1 # while문에 다시 들어가기 위해 절단기 높이 -1
print(temp + 1) #while문에서 빠져나왔다는 것은 절단기높이를 -1해줄 필요가 없다는 것이므로



