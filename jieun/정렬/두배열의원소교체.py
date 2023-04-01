N,K = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort() # 오름차순
arr_B.sort(reverse=True) # 내림차순
for i in range(K):
    arr_A[i] = arr_B[i]
    
ans = sum(arr_A)
print(ans)