#!/usr/bin/python
# Los Kundos 2015 - kunditos@gmail.com
#http://loskundos.blogspot.ie/2015/03/countdown-word-game-solver-python.html
import sys
import string
import copy

g_max_word_length = 9

def check_argument(argument):
    if len(argument) is not 2 or len(argument[1]) is not g_max_word_length:
        return False

    for c in argument[1]:
        if c not in string.ascii_lowercase:
            return False
    return True

def get_file_contents():
    file_s = open('wordsEn.txt', 'r')
    data = file_s.read()
    file_s.close()

    contents = []
    for item in data.split('\r\n'):
        if item and len(item) <= g_max_word_length:
            contents.append(item.lower())

    return contents

def is_word_possible(word, given_chars):
    wordchars = list(word)
    u_wordchars = copy.deepcopy(given_chars)

    for character in wordchars:
        if character in u_wordchars:
            u_wordchars[u_wordchars.index(character)] = ''
        else:
            return False

    return True

def find_words(given_chars):
    result = {}
    for word in get_file_contents():
        if is_word_possible(word, given_chars):
            chars = len(word)
            try:
                w_l = result[chars]
            except KeyError :
                w_l = []
            w_l.append(word)
            result[chars] = w_l

    return result

def output_results(results, given_chars):
    for index in reversed(range(1, g_max_word_length + 1)):
        max_word_list = results.get(index)

        if max_word_list:
            print ('Longest word(s) that could be found with input \'' + ''.join(given_chars) + '\' have ' + str(index) + ' letters:')
            print (', '.join(max_word_list))
        return

given_chars = []
if check_argument(sys.argv):
    given_chars = list(sys.argv[1])
else:
    print ('Give a string containing only letters and has length of ' + str(g_max_word_length))
    sys.exit(1)

results = {}
try:
    results = find_words(given_chars)
except KeyboardInterrupt :
    print ('\nBye')
    sys.exit(0)

output_results(results, given_chars)
