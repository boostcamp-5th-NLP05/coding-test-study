def solution():
    input_ = str(input())
    
    strings = []
    numbers = []
    
    for i in input_:
        if i.isdigit():                      #숫자 리스트에 추가
            numbers.append(int(i))                      
        else:                                #문자 리스트에 추가
            strings.append(i)                          
    
    strings.sort()                             #정렬
    num = sum(numbers)
    
    strings.append(str(num))                       #문자 리스트 뒤에 숫자 리스트 추가
    
    return ''.join(strings)                    #리스트를 다시 문자열로

solution()