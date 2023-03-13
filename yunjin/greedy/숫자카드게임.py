N, M = map(int, input().split())

arry = [list(map(int, input().split())) for n in range(N)]

r = []
for idx, value in enumerate(arry):
    r.append([idx, min(value)])

r.sort(key=lambda x:-x[1])

print(r[0][1])