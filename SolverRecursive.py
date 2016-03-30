import random
import itertools
wordMap = {}

def preprocess():
    count=0
    f = open('nineOrLess.txt', 'r')
    words = f.read().split()
    for word in words:
        key = sorted(word)
        sortedKey = "".join(key)
        count +=1
        addToMap(sortedKey,word)
    print(count)

def addToMap(key,value):
    if(len(key)>2 and len(key)<10):
        if key in wordMap:
            wordMap.get(key).append(value) #if key exists, get the reference to the list(value) and add it.
        else:
            wordMap.update({key:[value]})

preprocess()


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

def processWord(word):
    sortword = sorted(word)
    joinword = "".join(sortword)
    return joinword

def searcher(sortedLetters):
    count = 9
    for i in range(0, len(sortedLetters))
        perms += itertools.permutations(sortedLetters, count)
        count -=1
    print(list(perms))



def algoRunner():
    letters = getLetters()
    sortedLetters = processWord(letters)

    searcher(sortedLetters)

    result = 0
    return result

print(algoRunner())
