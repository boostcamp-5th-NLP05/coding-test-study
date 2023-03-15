data = input()

#code
#11101101011000001  10 -> 6/5 9-> 5/5 8-> 5/4
temp = data[0]
count = 0
for i in data:
    if temp != i:
        count += 1
        temp = i
if count%2 == 0:
    print(count//2)
else:
    print(count//2+1) 