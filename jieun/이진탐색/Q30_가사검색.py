from collections import defaultdict
# Trie 코드 참고: https://m.blog.naver.com/cjsencks/221740232900
class Node:
    def __init__(self, key):
        self.key = key
        self.cnt = defaultdict(int) # cnt[len]: 남은 길이가 len인 단어 개수
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        self.head.cnt[len(string)] += 1
        current_node = self.head
        
        
        for idx, char in enumerate(string):
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.cnt[len(string) - idx - 1] += 1
        
    def search(self, prefix, symb_len):
        # query: prefix + "?"" symb_len개
        # prefix 끝 노드에서 남은 길이가 symb_len인 단어 개수를 반환한다.
        current_node = self.head
        
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else: return 0
        
        return current_node.cnt[symb_len]
        

def find_question(query: str):
    # query 구조: "문자열???
    lo = -1
    hi = len(query)-1
    while lo+1 < hi:
        mid = (lo+hi)//2
        # 조건: is ? -> FFFTTT
        if query[mid] == "?":
            hi = mid
        else:
            lo = mid
    return hi

def solution(words, queries):
    answer = []
    
    trie = Trie()
    reverse_trie = Trie()
    
    for w in words:
        trie.insert(w)
        reverse_trie.insert("".join(reversed(w)))
        
    for q in queries:
        if q[0] == "?":
            q = "".join(reversed(q))
            idx = find_question(q)
            res = reverse_trie.search(q[:idx], len(q) - idx)
            answer.append(res)
        else:
            idx = find_question(q)
            res = trie.search(q[:idx], len(q) - idx)
            answer.append(res)

    return answer
