
def userInput(anagram):
    listword1 = list(anagram)
    sortword1 = sorted(listword1)
    joinword1 = "".join(sortword1)
    answer = hash(joinword1)
    return answer

def preprocess(anagram, wordList):
    #wordList = []
    f = open('wordsEn.txt', 'r')
    words = f.read().split()
    for word in words:
        if(len(word) == len(anagram)):
            wordList.append(word)
    return hasher(wordList)

def hasher(wordList):
    hashedWords=[]
    count = 0
    for word in wordList:
        listword = list(word)
        sortword = sorted(listword)
        joinword = "".join(sortword)
        hashedWords.append( hash(joinword))
        count+=1
    return hashedWords

def searcher(hashWord, hashedWords, wordList):
    resultList =[]
    counter = 0
    for hashedWord in hashedWords:
        if (hashedWord == hashWord):
            resultList.append(wordList[counter])
            #print(wordList[counter])
            #print(hashWord)
        counter +=1
    return resultList

def testalgo():
    #print("Enter any collection of letters:")
    #anagram = input()
    wordList = []
    anagram =  "farmer"
    hashWord = userInput(anagram)
    #print("all possible anagrams are as follows: ")
    hashedWords = preprocess(anagram, wordList)
    return searcher(hashWord, hashedWords, wordList)

if __name__=='__main__':
    print(testalgo())
    import timeit
    print(timeit.timeit("testalgo()",setup="from __main__ import testalgo", number = 100))
