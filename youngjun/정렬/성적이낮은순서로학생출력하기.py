def solution():
    N = int(input())
    dict_ = {}
    for _ in range(N):
        name, score = map(str,input().split())
        dict_[name] = int(score)
    
    sorted_dict = dict(sorted(dict_.items(), key=lambda x : x[1]))
    
    for i in list(sorted_dict.keys()):
        print(i, end = ' ')
    

solution()
    