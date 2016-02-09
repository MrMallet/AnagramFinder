wordList = []
hashedWords = []

def userInput():
    listword1 = list(anagram)
    sortword1 = sorted(listword1)
    joinword1 = "".join(sortword1)
    answer = hash(joinword1)
    return answer

def checker():
    f = open('wordsEn.txt', 'r')
    words = f.read().split()
    for word in words:
        if(len(word) == len(anagram)):
            wordList.append(word)

def hasher():
    count = 0
    for word in wordList:
        listword = list(word)
        sortword = sorted(listword)
        joinword = "".join(sortword)
        hashedWords.append( hash(joinword))
        count+=1

def searcher():
    counter = 0
    for hashWord in hashedWords:
        if (hashedWord == hashWord):
            print(wordList[counter])
            #print(hashWord)
        counter +=1

print("Enter any collection of letters:")
anagram = input()
hashedWord = userInput()
checker()
hasher()
print("all possible anagrams are as follows: ")
searcher()
