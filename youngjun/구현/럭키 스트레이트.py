def solution():
    score = int(input())
    
    cnt = 0                                                           
    front = 0                                                             
    back = 0
    
    for i in str(score):
        cnt+=1
        if cnt <= len(str(score))//2:      #왼쪽 
            front += int(i)                            
        else:                              #오른쪽
            back += int(i)                                 
    
    if front == back:                                     
        return 'LUCKY'                                     
    else:                                                                          
        return 'READY'                                     
                                                           
solution()