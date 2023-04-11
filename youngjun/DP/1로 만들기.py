d = [0] * 30001
d[0] = 30000      #d[0]을 30000으로
def div(n):
    
    d_2,d_3,d_5 = 0,0,0   #n이 2,3,5로 나누어 진다면 몫으로 변경
    
    if n == 1:
        return 0
    
    if d[n] != 0:
        return d[n]
    
    if n% 5 == 0:
        d_5 = n //5
    
    if n % 3 == 0:
        d_3 = n // 3
        
    if n % 2 == 0:
        d_2 = n //2
        
    d[n] = min(div(d_5),div(d_3),div(d_2),div(n-1)) + 1 #(가장 작은 값 + 1) 로 dp행렬 최신화
    
    return d[n]

div(int(input()))
    