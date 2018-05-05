import random

w = open('WordList.txt', 'r')
words = w.read()
word = words[0:]

split = word.split()
myWord1 = random.choice(split)
myWord2 = random.choice(split)
myWord3 = random.choice(split)

combinedWords = ''.join([myWord1, myWord2, myWord3])
print combinedWords

answer = raw_input("Would you like to generate another word? ")
while(answer == "Yes"):
    myWord1 = random.choice(split)
    myWord2 = random.choice(split)
    myWord3 = random.choice(split)
    combinedWords = ''.join([myWord1, myWord2, myWord3])
    print combinedWords
    break
