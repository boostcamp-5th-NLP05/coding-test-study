data = input()

#code

result = 0
for i in data:
    if i != '0' and result !=0 :
        result = result*int(i)
    else :
        result += int(i)
print(result)

