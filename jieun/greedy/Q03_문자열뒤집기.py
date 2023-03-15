S = input()

zero_cnt = 0  # 0 구간 개수
one_cnt = 0  # 1 구간 개수

# 0 구간 개수 찾기
# 구간은 [start, end)
start = 0
end = 0
while True:
    start = S.find("0", end)
    if start == -1:
        break
    zero_cnt += 1
    end = S.find("1", start)
    if end == -1:
        break

# 1 구간 개수 찾기
start = 0
end = 0
while True:
    start = S.find("1", end)
    if start == -1:
        break
    one_cnt += 1
    end = S.find("0", start)
    if end == -1:
        break

ans = min(zero_cnt, one_cnt)
print(ans)
