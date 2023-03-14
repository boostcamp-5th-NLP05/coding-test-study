s = str(input())

answer = 0

for i in s:
    
    if int(i) == 0 or int(i) == 1:
        answer += int(i)
        
    else:
        if answer == 0:
            answer += int(i)
        else:
            answer *= int(i)
print(answer)