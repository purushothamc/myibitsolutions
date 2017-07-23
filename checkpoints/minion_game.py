def minion_game(string):
    fp = open("/home/pchowdam/performance/input12.txt", "r")
    string = fp.read()
    vowels="aeiou".upper()
    consonants = "bcdfghjklmnpqrstvwxyz".upper()
    c1, c2, d1, d2 = 0, 0, {}, {}

    # no need to calculate all substrings :D
    # if we know a word starts with some letter,
    # count of all words starts with that letters = len(string) - index(where this word starting letter seen)
    #

    for idx, substring in enumerate(string):
        if substring[0] in consonants:
            c1 += len(string) - idx
        elif substring[0] in vowels:
            c2 += len(string) - idx
    """
    # earlier implementation
    for outIdx, char in enumerate(string):
        if char in consonants:
            for inIdx in range(outIdx, len(string)):
                temp = string[outIdx: inIdx+1]
                if not d1.get(temp, None):
                    d1[temp] = True
                    c1 += string.count(temp)
        elif char in vowels:
            for inIndx in range(outIdx, len(string)):
                temp = string[outIdx: inIdx+1]
                if not d2.get(temp, None):
                    d2[temp] = True
                    c2 += string.count(temp)
    """
    if c1 > c2:
        print "Stuart " + str(c1)
    elif c2 > c1:
        print "Kevin " + str(c2)
    else:
        print "Draw"

#string = "BANANA"
string = "guavaisanotherfruit       "
minion_game(string)