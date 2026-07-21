class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i in curr.children:
                curr = curr.children[i]
            else:
                new_node = TrieNode()
                curr.children[i]=new_node
                curr = new_node
        curr.endOfWord = True                                            

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i in curr.children:
                curr = curr.children[i]
            else:
                return False
        return curr.endOfWord                                

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i in curr.children:
                curr = curr.children[i]
            else:
                return False
        return True                        
        