N = int(input())

d = [0] * N #d는 왼쪽부터 (가로기준)i번째 칸을 채우는 갯수
d[0] = 1 #2X1 크기 덮개
d[1] = 1 + 2 #d[0]에 2X1덮개 + 1X2덮개2개 + 2X2덮개 1개 

for i in range(2, N):
     d[i] = d[i - 2]*2 + d[i - 1]
print(d[i])