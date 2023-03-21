def solution():
    n = str(input())
    answer = 8                #나이트가 움직일 수 있는 방법 총 8개
    x = ord(n[0]) - ord('a')  #아스키코드를 통해 x좌표 숫자로 변경
    y = int(n[1]) -1
    
    moves = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]] #움직였을 때 x,y 좌표 변화량
    
    for move in moves:                          #x 또는 y가 밖으로 나간다면 answer 에서 -1씩
        if x + move[0] < 0 or x + move[0] > 7:
            answer -= 1
            continue
        if y + move[1] < 0 or y + move[1] > 7:
            answer -= 1
            continue
    return answer

solution()