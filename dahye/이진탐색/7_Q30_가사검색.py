import bisect
import collections

def func(x,left,right): # bisect로 해당 단어 개수 구하기
    left_idx = bisect.bisect_left(x,left)
    right_idx = bisect.bisect_right(x,right)

    return right_idx - left_idx

def solution(words, queries):
    answer = []
    # 단어 길이 순으로 분리하기위해 딕셔너리 생성
    dic1 = collections.defaultdict(list)
    dic2 = collections.defaultdict(list)
    for word in words:
        # 단어 길이 순으로 분리
        dic1[len(word)].append(word)
        dic2[len(word)].append(word[::-1])


    #정렬
    for key in dic1.keys():
        dic1[key].sort()
        dic2[key].sort()

    for query in queries:
        # 앞에 ?가 붙은 경우
        if query[0] != '?':
            answer.append(func(dic1[len(query)],query.replace('?','a'),query.replace('?','z')))

        # 뒤에 ?가 붙은 경우
        else :
            query = query[::-1]
            answer.append(func(dic2[len(query)],query.replace('?','a'),query.replace('?','z')))
    return answer



# def solution(words, queries):
#     answer = []
    
#     for wild in queries:
#         count = 0
#         for y in words:
#             if len(wild) == len(y):
#                 i = 0
#                 check = True
#                 for i in range(len(wild)):
#                     if wild[i] != '?':
#                         if wild[i] != y[i]:
#                             check = False
#                             break
#                 if i == len(wild) - 1 and check == True:
#                     count += 1
        
#         answer.append(count)
#     return answer


# words = input()
# queries = input()

# words.sort()

# print(solution(words, queries))