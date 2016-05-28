import time # Used for time delay function
import csv # Used for csv handling
import nltk # Used for natural language recognition
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)
from nltk.corpus import wordnet # Wordnet for finding synonyms

from random import randint # Used to generate random integer

import ASCII_Store

# Dictionary containing information about user
userData = {}

# Used to reveal text with the time delay
def reveal(text):
    time.sleep(1)
    print "FD: " + text

# Used to reveal text without the time delay
def revealInstant(text):
    time.sleep(1)
    print "FD: " + text

# Used to reveal text without Time Delay and "FD: "
def revealFree(text):
    print text

# Removes excessive spaces, returns cleaned
def clean(string):
    sList = string.split()
    nString = ""
    for word in sList:
        nString += (word + " ")
    return nString[0:-1] # skips last space

# Initial lines when started
def intro():
    reveal("Hey there, my name is Friendly-Drink, but I go by FD.")
    reveal("But I go by FD")
    getName()

# Gets name of user
def getName():
    reveal("What's your name?")
    userData['userName'] = raw_input('> ') # input stored in user data dictionary
    reveal("Hey there %s, it's nice to meet you" % userData['userName'])

# function to print time of a location from user input using Dataset
def getTime(locale):
    locale = clean(locale)
    searchParam = locale.lower()

    reveal("Let me look up the time in %s" % locale.title())

    # Opens files used for determining time zone information
    f0 = open('../friendly-drink/Datasets/timezonedb/country.csv')
    countryTable = csv.reader(f0)

    f1 = open('../friendly-drink/Datasets/timezonedb/zone.csv')
    zone = csv.reader(f1)

    f2 = open('../friendly-drink/Datasets/timezonedb/timezone.csv')
    timezone = csv.reader(f2)

    # Finds city in list of time zones
    for row in zone:
        if searchParam in row[2].lower():
            zone_id = row[0] # zone_id used for lookup in timezone.csv
            countryCode = row[1] # countryCode

    # Throws error if city not found
    if 'zone_id' not in locals():
        reveal("I can't find that place")
        return

    # Finds country using previous country code
    for row in countryTable:
        if row[0] == countryCode:
            countryName = row[1] # Full name of country is saved

    # Determines GMT Offset
    for row in timezone:
        if (zone_id == row[0]): # still need to account for DST
            # gets time difference and converts to num
            GMTOffset = int(row[3]) # Offset from GMT
            break

    checkTime = time.time() + GMTOffset # gets time in desired locale

    # Print results
    reveal("The time in %s, %s is:" % (searchParam.title(), countryName))
    reveal(time.strftime("%H:%M:%S, %a, %d %b %Y ", time.gmtime(checkTime)))

# Finds synonyms of word - returns array of synonyms
def findSynonyms(entryWord):
    # Array which will contain synonyms
    synonyms = []
    for syn in wordnet.synsets(entryWord):
        # Iterates through synonyms
        for l in syn.lemmas():
            # Iterates through possible lemmas, appends to synonyms array
            synonyms.append(l.name())
    return synonyms

# Checks if asking to flip a coin
def checkToFlipCoin(POS_tagged_sentence):
    # finds synoynms of the words 'flip' and 'toss'
    flipSynonyms = findSynonyms("flip") + findSynonyms("toss")

    for word in POS_tagged_sentence:
        if word[1] == 'NN': # Checks if word is a noun
            if WordNetLemmatizer().lemmatize(word[0]) == 'coin':
                # Proceed if 'coin' is in setence
                for words in POS_tagged_sentence:
                    if words[1] == 'VB' or words[1] == 'NN' or words[1] == 'IN':
                        # Proceed if a word is base verb, preposition or singular noun
                        for syns in flipSynonyms:
                            # Iterates through synonyms from before
                            if syns == words[0]:
                                # If word is a synonym, return True
                                return True

# Flips coin, prints string showing answer
def flipCoin():
    reveal("*Flipping a coin*")
    checkVal = randint(0,1)

    if checkVal == 1:
        # Heads case
        revealFree(ASCII_Store.artFiles['heads']) # Print ASCII
        revealFree("Heads!")
    else:
        # Tails case
        revealFree(ASCII_Store.artFiles['diamond']) # Print ASCII
        revealFree("Tails!")


# tokenizes string to determine if user is asking to flip a coin
def searchQ(sentence):
    tokens = nltk.word_tokenize(sentence) # Array of sentence
    usedWords = [] # Contains all the words used to make decisions on what response to make
    tags = nltk.pos_tag(tokens) # Array containing all words and POS tag

    flipCheck = checkToFlipCoin(tags)
    if flipCheck:
        usedWords.extend(['flip','coin'])
        flipCoin()

def start():
    sTime = time.time() # time from program start
    intro()
    while True:
        qString = raw_input('> ') # Query string
        if qString.startswith("Time in"):
            getTime(qString[7:])
        elif qString == "end":
            break
        else:
            searchQ(qString)

start()
