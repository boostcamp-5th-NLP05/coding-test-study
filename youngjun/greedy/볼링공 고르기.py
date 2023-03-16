import math

def Solution():
    n, m = map(int, input().split())
    balls = list(map(int, input().split()))
    
    ball_type = list(set(balls))
    answer = math.comb(n,2) #모든 조합 개수
    
    for i in ball_type:
        answer -= math.comb(balls.count(i),2) #중복된 경우 만큼 뺴주기
    
    return answer
        
Solution()