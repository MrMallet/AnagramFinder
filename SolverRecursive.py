import timeit
import random
import itertools
from itertools import combinations

wordDict = dict()

def preprocess():
    count=0
    f = open('nineOrLess.txt', 'r')
    words = f.read().split()
    for word in words:
        key = sorted(word)
        sortedKey = "".join(key)
        count +=1
        addToMap(sortedKey,word)

def addToMap(key,value):
    if(len(key)>2 and len(key)<10):
        if key in wordDict:
            wordDict.get(key).append(value) #if key exists, get the reference to the list(value) and add it.
        else:
            wordDict.update({key:[value]})

preprocess()

vowels =['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o','u','u','u','u',]   #no weightin in either forthe minute
consts =['q','w','w','r','r','r','r','r','r','t','t','t','t','t','t','y','y','p','p','s','s','s','s','d','d','d','d','f','f','g','g','g','j','k','l','l','l','l','z','x','c','c','v','v','b','b','n','n','n','n','n','n','m','m',]
#two arrays above weighted using scrabble weighting
numOfVowels = 3
numOfConsts = 4
checkAnswerCounter = 9

def getLetters():
    letters=[]
    for i in range(numOfVowels):
        letters.append(random.choice(vowels))
    for i in range(numOfConsts):
        letters.append(random.choice(consts))
    for i in range(2):
        letters.append(random.choice(vowels + consts))
    return letters

def processWord(word):
    sortword = sorted(word)
    joinword = "".join(sortword)
    return joinword

def searcher(sortedLetters):
    count = 9
    #print (len(sortedLetters))
    combs = []
    comb= []
    for i in range(0, count):
        combs = itertools.combinations(sortedLetters, count)
        comb = ["".join(line) for line in combs]
        count -=1
        for combination in comb:
            if combination in wordDict.keys():
                return(wordDict[combination])

def algoRunner():
    letters = getLetters()
    sortedLetters = processWord(letters)
    result =searcher(sortedLetters)
    return result

if __name__=='__main__':
    print(algoRunner())
    import timeit
    print(timeit.timeit("algoRunner()",setup="from __main__ import algoRunner", number = 10000))

#print(algoRunner())
#print(searcher(processWord('parse')))
