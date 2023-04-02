N, K = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.sort() #작은수부터정렬
for i in range(K):
    A.sort(reverse = True) #큰 수부터 정렬 *계속 append하므로 for문마다 정렬
    if min(A) < max(B): 
        A.pop()
        A.append(B.pop()) #바꿔치기
    else:
        break
print(sum(A))


