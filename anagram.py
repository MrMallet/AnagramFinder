f = open('wordsEn.txt', 'r')

words = f.read().split()

anagram = input()
listword1 = list(anagram)
sortword1 = sorted(listword1)
joinword1 = "".join(sortword1)
hashedword = hash(joinword1)

count = 0
counter = 0
hashedNines = []
for word in words:
    listword = list(word)
    sortword = sorted(listword)
    joinword = "".join(sortword)
    hashedNines.append( hash(joinword))
    count+=1
    #print(word)
#print(hashedword)
for hashNine in hashedNines:

    if hashedword == hashNine:
        print(words[counter])
        print(hashNine)
    counter +=1
#print(count)
