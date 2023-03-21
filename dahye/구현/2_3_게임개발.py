n, m = map(int, input().split())
loc1, loc2, dir = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

now = [loc1, loc2]
while True:
    if dir == 0:
        
