import time # Used for time delay function
import csv # Used for csv handling
import nltk # Used for natural language recognition
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)
from nltk.corpus import wordnet # Wordnet for finding synonyms
from nltk.tokenize import sent_tokenize, word_tokenize

from findsynonyms import findSynonyms
from location import lctnwthrgt
from stateofmind import fnchk
from random import randint # Used to generate random integer

import ASCII_Store
import databanksearch as dbsearch # file containing db query searches

# Dictionary containing information about user
userData = {}

# Temporary storage for informaton
tempstore= {}
sombin= 2;

# Used to reveal text with the time delay
def reveal(text):
    time.sleep(0)
    print "FD: " + text

# Used to reveal text without the time delay
def revealInstant(text):
    time.sleep(0)
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
    #Gets weather data and location data
    (userData['temperature'], userData['wndspd'], userData['wthrid'],
    userData['city'])=lctnwthrgt()
    getName()

# Gets name of user
def getName():
    reveal("What's your name?")
    userData['userName'] = raw_input('> ').title() # input stored in user data dictionary
    reveal("Hey there %s, it's nice to meet you" % userData['userName'])
    getSchool()
#School information
def getSchool():
    reveal("So which college do you go to?")
    userData['College']= raw_input('> ')
    reveal("Holy shit! You go to %s, that's a really good place." %userData['College'])
    howdy()
#Getting State of Mind
def howdy():
    reveal("How are you?")
    tempstore['sttofmnd']= raw_input('> ')
    stateofmind()

#Finding State of Mind
def stateofmind():
    usedWords = [] # Contains all the words used to make decisions on what response to make
    wrdarr = word_tokenize(tempstore['sttofmnd']) # Array of sentence
    tokens= nltk.pos_tag(wrdarr)


    if fnchk(tokens):
        reveal ("That is Amazing.")
        sombin=1
    else:
        reveal ("I hope you feel better")
        sombin=0



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


# Checks if asking to flip a coin
def checkToFlipCoin(POS_tagged_sentence):
    # finds synoynms of the words 'flip' and 'toss'
    flipSynonyms = findSynonyms("flip") + findSynonyms("toss")

    for word in POS_tagged_sentence:
        # print WordNetLemmatizer().lemmatize(word[0])
        # print word[1]
        if word[1] == 'NN' or word[1] == 'NNS': # Checks if word is a noun(or pl.)
            if WordNetLemmatizer().lemmatize(word[0]) == 'coin':
                # Proceed if 'coin' is in sentence
                for words in POS_tagged_sentence:
                    if words[1] == 'VB' or words[1] == 'NN' or words[1] == 'IN':
                        # Proceed if a word is base verb, preposition or singular noun
                        for syns in flipSynonyms:
                            # Iterates through synonyms from before
                            if syns == words[0]:
                                # If word is a synonym, return True
                                return True
            elif WordNetLemmatizer().lemmatize(word[0]) == 'head':
                # Proceed if 'head' is in sentence
                for word in POS_tagged_sentence:
                    # iterates through other nouns in sentence
                    if word[1] == 'NN' or word[1] == 'NNS':
                        if WordNetLemmatizer().lemmatize(word[0]) == 'tail':
                            # Proceeds if sentence contains 'tail'
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

# a fucntion to check if user is asking for weather {VERY INCOMPLETE}
def weathercheck(sentence):
    return True

def weatherout():
    weather='The temperature in %s is %5.2f with wind speed of %4.1f' %(userData['city'], userData['temperature'], userData['wndspd'])
    reveal(weather)

# tokenizes string to determine if user is asking to flip a coin
def searchQ(inString):
    sentence = inString.lower()
    tokens = nltk.word_tokenize(sentence) # Array of sentence
    usedWords = [] # Contains all the words used to make decisions on what response to make
    tags = nltk.pos_tag(tokens) # Array containing all words and POS tag

    if checkToFlipCoin(tags):
        usedWords.extend(['flip','coin'])
        flipCoin()
    elif weathercheck(tags):
        weatherout()
    else:
        dbsearch.search(inString)

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
