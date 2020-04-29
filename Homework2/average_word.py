"""
Calculate average number of words from input
"""

#import random module
import random
numWords = random.randint(3, 6)

#announce random number of words needed
print("I need " + str(numWords) + " words:")

#initializing variables
wordCounter = 1
longestWord = ""
shortestWord = ""
totalLength = 0

#main user input loop
while wordCounter <= numWords:
    introWord = input("Word #" + str(wordCounter) + " please! ")
    #make sure that shortestWord is not replaced unintentionally
    if wordCounter < 2:
        shortestWord = str(introWord)

    #for use in later calculation (averageWordLength)
    wordCountLength = len(introWord)
    totalLength += wordCountLength

    #check if longest / shortest word
    if len(introWord) > len(longestWord):
        longestWord = str(introWord)
    elif len(introWord) < len(shortestWord):
        shortestWord = str(introWord)

    #check for duplicate words
    if len(introWord) == len(longestWord):
        longestWord = str(introWord)
    if len(introWord) == len(shortestWord):
        shortestWord = str(introWord)
    if introWord == longestWord and introWord == shortestWord:
        introWord = str(longestWord)
        introWord = str(shortestWord)

    #accumulator
    wordCounter += 1

#word length average calculation
averageWordLength = totalLength / numWords

#final print
print("====")
print("Shortest: " + str(shortestWord))
print("Longest: " + longestWord)

#cut off repeating numbers
averagePrint = format(averageWordLength, '>,.2f')
print("Average Length: " + averagePrint)
