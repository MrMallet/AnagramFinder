### James Moloney
#### G00304978

# Countdown Letters Game Solver
Creating an algorithm that solves the nine letter Countdown game according to the rules of the game.
Also to create the wordlist used in the project but for the mean time we'll use wordsEn.txt.


## Background
The first task I completed as part of this project was to Google "countdown letters game solver".
Google gave me two relevant results on the first page, these are [Countdown solver][1] and [Countdown letters game solver][2].
The rules of the game are to be found [here][4]


## Words list
My words list is in the file [wordsEN.txt](wordsEn.txt) in this repository/gist.
I got my words list from the [English Wordlists ][3] website.
However my list of 9 (and less than) letter wordlist is [nineOrLess.txt][nineOrLess.txt]


## Python script
My script is in the files [solver.py](solver.py) in this repository and it works as follows.
The most important section is:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
First run is a brute force Quadratic solution. 9*8*7*6 = 3024 searches through the wordlist in the worst of cases.
On a machine with 6300 AMD(Six cores and 4ghz) processor it runs slow searching for the five letter words when it gets down that far.


Using the itertools.combination allows
nCr  =  	n!
     -----------
    	r!(n - r)!

9C9 = 1           1
9C8 = 9           10
9C7 = 36          46
9C6 = 84          130
9C5 = 126         256
9C4 = 126         382
9C3 = 84          466
9C2 = 36          502 possible maximum iterations
9C1 = 9           511  

http://www.mathcelebrity.com/permutation.php?num=9&den=3&pl=Combinations


## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Countdown letters game.
Testing on 10000 calls without preprocessing takes 1.2 seconds



## References
[1]: http://incoherency.co.uk/countdown/
[2]: http://datagenetics.com/blog/august52014/index.html
[3]: http://www-01.sil.org/linguistics/wordlists/english/
[4]: https://en.wikipedia.org/wiki/Countdown_(game_show)#Letters_round
