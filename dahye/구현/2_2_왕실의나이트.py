loca = input()

#code

check1 = ['a','h'] #check1로 시작하면 수직-수직-수평 2가지, 수평-수평-수직 2가지 경우 이동 불가능 -4
check2 = ['b','g'] #check2로 시작하면 수평-수평-수직 2가지 경우 이동 불가능 -2
check3 = ['1','8'] #check3으로 끝나면 수직-수직-수평 2가지, 수평-수평-수직 2가지 경우 이동 불가능 -4
check4 = ['2','7'] #check4으로 끝나면 수평-수평-수직 2가지 경우 이동 불가능 -2

result = 8

if loca[0] in check1:
    if loca[1] in check3:
        print(result-4-4+2) #check1,3 2개 중복해서 제외했으므로 +2
    elif loca[1] in check4:
        print(result-4-2+1) #check1,4 1개 중복해서 제외했으므로 +1
    else:
        print(result-4)
elif loca[0] in check2:
    if loca[1] in check3:
        print(result-2-4+1) #check2,3 1개 중복해서 제외했으므로 +1
    elif loca[1] in check4:
        print(result-2-2) 
    else:
        print(result-2)
else:
    if loca[1] in check3:
        print(result-4)
    elif loca[1] in check4:
        print(result-2) 
    else:
        print(result) #check에서 해당이 안된다면 총 가능한 경우의수 8 출력

