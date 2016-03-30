import random
#append to listofanswers as we check the nine letter answers
#in checking the eight letter answers we will have to change the the list of eight letter wordlist amd so on


wordList = []
resultList =[]
hashedWords=[]
letters=[]
vowels =['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o','u','u','u','u',]   #no weightin in either forthe minute
consts =['q','w','w','r','r','r','r','r','r','t','t','t','t','t','t','y','y','p','p','s','s','s','s','d','d','d','d','f','f','g','g','g','j','k','l','l','l','l','z','x','c','c','v','v','b','b','n','n','n','n','n','n','m','m',]
#two arrays above weighted using scrabble weighting
numOfVowels = 3
numOfConsts = 4
checkAnswerCounter = 9

def getLetters():
    for i in range(numOfVowels):
        letters.append(random.choice(vowels))
    for i in range(numOfConsts):
        letters.append(random.choice(consts))
    for i in range(2):
        letters.append(random.choice(vowels + consts))
    return letters

getLetters()
print(letters)

def sortLetters(letters):
    #listword1 = list(anagram)
    sortword1 = sorted(letters)
    #print(sortword1)
    joinword1 = "".join(sortword1)
    #print(joinword1)
    answer = hash(joinword1)
    #print(answer)
    return answer

def processWordToHash(word):
    sortword = sorted(word)
    joinword = "".join(sortword)
    hashedAnagram = hash(joinword)
    return hashedAnagram

def preprocess(wordList):
    #wordList = []
    f = open('nineOrLess.txt', 'r')
    words = f.read().split()
    for word in words:
        #if(len(word) == len(anagram)):
        wordList.append(word)
    return hasher(wordList)

def hasher(wordList):
    #hashedWords=[]
    count = 0
    for word in wordList:
        listword = list(word)
        hashedWords.append(processWordToHash(listword))
        count+=1
    return hashedWords

def searcher(hashWord, hashedWords, wordList):
    counter = 0
    for hashedWord in hashedWords:
        if (hashedWord == hashWord):
            resultList.append(wordList[counter])
        counter +=1
    return resultList

def checkAnswer(answer):
    if not answer :
        #print("sure were getting here at least")
        #reduce length of the array by popping one off the left and search with that word,
        #repeat and rinse until wever removed and seacrhed all possible eigth letter words
        #
        subAns= list(letters)
        print("to the possible 8s ")
        for i in range(len(subAns)):
            answer8= subAns[0:(i)] + subAns[(i+1):]
            hashed8Anagram = processWordToHash(answer8)
            answer = searcher(hashed8Anagram, hashedWords, wordList)

    if not answer:
        #place a recursive call in here
        print("to the possible 7s")
        for i in range(len(letters)):
            answer8 = letters[0:(i)] + letters[(i+1):]
            for j in range(len(answer8)):
                answer7 = answer8[0:(j)] + answer8[(j+1):]
                hashed7Anagram = processWordToHash(answer7)
                answer = searcher(hashed7Anagram, hashedWords, wordList)
    if not answer:
        print("to the possible 6s")
        for i in range(len(letters)):
            answer8 = letters[0:(i)] + letters[(i+1):]
            for j in range(len(answer8)):
                answer7 = answer8[0:(j)] + answer8[(j+1):]
                for k in range(len(answer7)):
                    answer6 = answer7[0:(k)] + answer7[(k+1):]
                    hashed6Anagram = processWordToHash(answer6)
                    answer = searcher(hashed6Anagram, hashedWords, wordList)
    if not answer:
        print("to the possible 5s")
        for i in range(len(letters)):
            answer8 = letters[0:(i)] + letters[(i+1):]
            for j in range(len(answer8)):
                answer7 = answer8[0:(j)] + answer8[(j+1):]
                for k in range(len(answer7)):
                    answer6 = answer7[0:(k)] + answer7[(k+1):]
                    for l in range(len(answer6)):
                        answer5 = answer6[0:(l)] + answer6[(l+1):]
                        hashed5Anagram = processWordToHash(answer5)
                        answer = searcher(hashed5Anagram, hashedWords, wordList)
    return answer




def testalgo():
    #wordList = []
    hashWord = processWordToHash(letters)
    hashedWords = preprocess(wordList)
    answer = searcher(hashWord, hashedWords, wordList)

    checkAnswer(answer)
    resultSet = set(answer)
    return resultSet


print(testalgo())
