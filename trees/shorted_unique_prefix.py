from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.end_of_word = False
        self.count = 0

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch in current.children:
                current = current.children[ch]
                current.count += 1
            else:
                new_node = TrieNode()
                current.children[ch] = new_node
                current = new_node
                current.count = 1
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch in current.children:
                current = current.children[ch]
            else:
                return False
        if current.end_of_word:
            return True
        return False

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        dd = defaultdict(list)
        trie = Trie()
        result = list()

        for word in A:
            trie.insert(word)

        for word in A:
            temp = list()
            current = trie.root
            for index, ch in enumerate(word):
                if current.count == 1:
                    result.append("".join(temp))
                    break
                else:
                    temp.append(ch)
                    current = current.children[ch]
                    if not current.children:
                        result.append("".join(temp))
                        break
        return result

A = ["zebra", "dog", "duck", "dove"]
#A = [ "bearcat", "bert" ]
B = Solution()
print B.prefix(A)
