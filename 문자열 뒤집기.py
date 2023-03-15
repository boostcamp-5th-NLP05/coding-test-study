def Solution():
    
    s = str(input())
    #첫 숫자에서 다른 숫자로 몇 번 바뀌었는지 찾는 문제. 0으로 시작한다면 '01'의 개수 1로 시작한다면 '10'의 개수
    return max(s.count('01'), s.count('10')) 
    
Solution()