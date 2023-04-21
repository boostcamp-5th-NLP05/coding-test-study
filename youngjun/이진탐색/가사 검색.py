from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    
    front_words = sorted(words,key = lambda x:(len(x),x))
    ord_front_words = []
    for i in words:
        tmp = []
        for j in i:
            tmp.append(ord(j))
        ord_front_words.append(tmp)
        
    back_words = sorted(words,key = lambda x:(len(x),x[::-1]))
    ord_back_words = []
    for i in words:
        tmp = []
        for j in i:
            tmp.append(ord(j))
        ord_back_words.append(tmp)
        
    len_words = [len(i) for i in front_words]
    
    lo_len = len(front_words[0])
    hi_len = len(front_words[-1])
    
    for i in queries:
        start = bisect_left(len_words,len(i))
        end = bisect_right(len_words,len(i))
        
        if i[0] == '?' and i[-1] == '?': #모든 문자가 ?일 때
            answer.append(end-start)
            continue
        
        #elif i[0] != '?':
        #    idx = 0
        #    lo = start
        #    hi = end
        #    while i[idx] != '?':
        #        tmp_list = ord_front_words[lo:hi]
        #        for word in tmp_list:
        #            word[idx]
        #
        #else:

    return 