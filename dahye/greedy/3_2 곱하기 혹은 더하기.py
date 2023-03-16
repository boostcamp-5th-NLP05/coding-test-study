data = input()

#code

result = 0
for i in data:
    i = int(i)
    if i == 0 or i == 1 or result == 0 or result == 1 :
        result += i
    else :
        result = result * i
print(result)

