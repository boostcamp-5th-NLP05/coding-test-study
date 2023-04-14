n = int(input())
cnt = 1
num = 2
while True:
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        cnt += 1
    else:
        num += 1
        continue
        
    if cnt == n:
        print(num)
        break
    num += 1