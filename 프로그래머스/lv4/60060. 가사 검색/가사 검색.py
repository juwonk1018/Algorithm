class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root
        cur.count += 1
        for w in word:
            if(cur.children.get(w) == None):
                cur.children[w] = Node()
            
            cur = cur.children[w]
            cur.count += 1
            
    def search(self, word):
        cur = self.root
        for w in word:
            if(cur.children.get(w)):
                cur = cur.children[w]
            else:
                return 0
        return cur.count
    
def solution(words, queries):
    answer = []
    
    trie = [Trie() for _ in range(10001)]
    reverseTrie = [Trie() for _ in range(10001)]
    for word in words:
        trie[len(word)].insert(word)
        reverseTrie[len(word)].insert(word[::-1])
    
    for query in queries:
        if(query[0] != "?"):
            answer.append(trie[len(query)].search(query.replace("?", "")))
        elif(query[0] == "?"):
            answer.append(reverseTrie[len(query)].search(query.replace("?", "")[::-1]))
    return answer