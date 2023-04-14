n = int(input())
cnt = 1
d = [1]
i_2,i_3,i_5 = 0,0,0

while cnt != n:
    mul_2 = 2*d[i_2]
    mul_3 = 3*d[i_3]
    mul_5 = 5*d[i_5]
    
    min_num = min(mul_2,mul_3,mul_5)
    
    d.append(min_num)
    cnt+=1
    
    if mul_2 == min_num:
        i_2 += 1
    if mul_3 == min_num:
        i_3 += 1
    if mul_5 == min_num:
        i_5 += 1

print(d[-1])