wordList = []
hashedWords = []
sortword1 = " "

def userInput():
    listword1 = list(anagram)
    sortword1 = sorted(listword1)
    joinword1 = "".join(sortword1)
    answer = hash(joinword1)
    return answer

def eliminate():
    #take the sorted word minus 1 letter from position[i] and search for length-1
    #take the sorted word minus 2 letters from position[i] + and postion[j] and search from length -2
    #take the sorted word minus 3 letters from position[i,j,k] icrementing the k and search from length-3
    #absolutely untenable scenario. the larger the word the more impossible it becomes. Quadratic.
    #would have to use an interative algorithm in conjunction with this one.
    #OR completely change plan of attack.
    
    i=0
    j= len(anagram)
    for i in j-1:
        listword2 = list(sortword1)# trying to create the list minus last one.


def checker():
    f = open('wordsEn.txt', 'r')
    words = f.read().split()
    for word in words:
        if(len(word) <= len(anagram)):
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
