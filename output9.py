f = open('wordlist.txt', 'r')
o = open('nineOrLess.txt', 'w')

for word in f:
  word = word.strip()
  if len(word) < 10:
    o.write(word + "\n")
