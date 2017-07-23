from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.end_of_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch in current.children:
                current = current.children[ch]
            else:
                new_node = TrieNode()
                current.children[ch] = new_node
                current = new_node
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

def hotel_reviews(A, B):
    dd = defaultdict(list)
    trie = Trie()

    good_words = A.split("_")
    for word in good_words:
        trie.insert(word)

    reviews = B
    for index, review in enumerate(reviews):
        review = review.split("_")
        count = 0
        for word in review:
            if trie.search(word):
                count += 1
        dd[count].append(index)
    keys = sorted(dd.keys(), reverse=True)
    result = list()
    for key in keys:
        result.extend(dd[key])
    return result

s = "cool_ice_wifi"
r = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]

print hotel_reviews(s, r)