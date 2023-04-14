A = list(input())
B = list(input())

d = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)] #공백부터 시작

for i in range(len(A)+1):
    d[i][0] = i # A의 0번째 단어(공백)가 B의 0부터 i번째 단어가 되기 위한 편집거리 수 update
for j in range(len(B)+1):
    d[0][j] = j # B의 0번째 단어(공백)가 A의 0부터 i번째 단어가 되기 위한 편집거리 수 update

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]: # 교체를 할 필요가 없을 때 (A와B는 인덱스를 0부터 count해주므로 -1씩)
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1])
        else:
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+1) # 삭제, 삽입, 교체 중 작은 것 선택

print(d[-1][-1])


#감이 잡히지 않아 2차원 list로 해결하는 아이디어를 참고하였습니다.