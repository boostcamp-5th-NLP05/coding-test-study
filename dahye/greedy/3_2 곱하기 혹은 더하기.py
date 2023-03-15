data = input()

#code

result = 0
for i in data:
    i = int(i)
    if i == 0 or result ==0 or i == 1 or result == 1 : 
        #result가 1인 상황도 +가 더 크다는 것을 고려
        result += i
    else :
        result = result * i
print(result)

