import timeit
import random
import itertools
from itertools import combinations

wordDict = dict() #https://docs.python.org/2/library/stdtypes.html#dictionary-view-objects

def processWord(word):
    sortword = sorted(word)
    joinword = "".join(sortword)
    return joinword

def preprocess():
    count=0
    f = open('nineOrLess.txt', 'r')
    words = f.read().split()
    for word in words:
        sortedKey = processWord(word)
        count +=1
        addToDic(sortedKey,word)

def addToDic(key,value):
    if(len(key)>2 and len(key)<10):
        if key in wordDict:
            wordDict.get(key).append(value)
        else:
            wordDict.update({key:[value]})

preprocess()

vowels =['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o','u','u','u','u',]   #no weightin in either forthe minute
consts =['q','w','w','r','r','r','r','r','r','t','t','t','t','t','t','y','y','p','p','s','s','s','s','d','d','d','d','f','f','g','g','g','j','k','l','l','l','l','z','x','c','c','v','v','b','b','n','n','n','n','n','n','m','m',]
#two arrays above weighted using scrabble weighting
numOfVowels = 3
numOfConsts = 4

def getLetters():
    letters=[]
    for i in range(numOfVowels):
        letters.append(random.choice(vowels))
    for i in range(numOfConsts):
        letters.append(random.choice(consts))
    for i in range(2):
        letters.append(random.choice(vowels + consts))
    return letters

def searcher(sortedLetters):
    count = (len(sortedLetters))
    #print (len(sortedLetters))
    combs = []
    comb= []
    for i in range(0, count):
        combs = itertools.combinations(sortedLetters, count)
        #this allows for a maximum of 9c9+c98+9c7+.... which comes to a totol of 502 maximum calls to the
        comb += ["".join(line) for line in combs]
        count -=1
        for combination in comb:
            #print (combination)
            if combination in wordDict.keys():
                return(wordDict[combination])

def algoRunner():
    letters = getLetters()
    print(letters)
    sortedLetters = processWord(letters)
    result =searcher(sortedLetters)
    return result

# if __name__=='__main__':
#     print(algoRunner())
#     import timeit
#     print(timeit.timeit("algoRunner()",setup="from __main__ import algoRunner", number = 10000))

print(algoRunner())
#print(searcher(processWord('education')))
