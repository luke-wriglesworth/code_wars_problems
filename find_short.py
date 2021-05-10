def find_short(s):
    wordList=s.split()
    shortestLength=len(wordList[0])
    for word in wordList:
        if len(word)<shortestLength:
            shortestLength=len(word)
        else:
            continue
    return shortestLength