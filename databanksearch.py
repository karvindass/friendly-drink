import nltk # Used for Natural Language Processing
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)
from nltk.tokenize import sent_tokenize, word_tokenize # Used to sentence and word tokenize

import rdflib # Import for dbpedia usage
from rdflib import Graph, URIRef # Used to make dbpedia queries
from rdflib import RDFS # Used to get label name in dbpedia

from friendly_drink import findSynonyms # Used to find synonyms

def check(personName):
    g=rdflib.Graph()
    g.load('http://dbpedia.org/resource/Semantic_Web')

    for s,p,o in g:
        print s,p,o

# Get Birthday of resource
def getBirthday(rdfFile):
    g = Graph() # Creates graph object
    g.parse(rdfFile) # Parses through rdfFile
    generator = g.objects(predicate = RDFS.label) # Creates object of all labels given in all languages

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")): # finds subjects and objects with predicate of birthDate
        return stmt[1] # Returns first value found

# Find label function
# Determine's label name based on resource given
def getLabel(rdfFile):
    g = Graph() # Creates graph object
    g.parse(rdfFile) # Parses through rdfFile

    generator = g.objects(predicate = RDFS.label) # Creates object of all labels given in all languages

    for stmt in generator: # loops through all labels in all languages
        if stmt.language == "en":
            return stmt # Returns the English name for the resource

# Gen Resource string
# Should find the link to the object of the interested thing
# e.g. Kanye
def getResource(resName):
    resName = resName.title()
    tokens = nltk.word_tokenize(resName)
    qString = "http://dbpedia.org/resource/" + tokens[0]
    for i in range(1, len(tokens)):
        qString += "_" + tokens[i]

    return qString

# Parse question, identify what is asked and return results
# Input is string
# string is processed by sentence
def parseQuestion(fullString):
    sentenceArray = sent_tokenize(fullString)

    for sentence in sentenceArray:
        qIndex = qQuestion(sentence)
        if qIndex == 3: # 'When' question
            whenQuestion(sentenceArray)

# Identifies what kind of question it is asking  (Who/What/Where/When/What/How)
def qQuestion(querySentence):
    wordsInSentence = word_tokenize(querySentence)
    qWords = ['who','what','where','when','what','how']

    for word in wordsInSentence:
        if word in qWords:
            return qWords.index(word)

# When question
# from output of above question, will scan for time frame and all
# Identifies time request it is making
# Makes request to object identifier
# Does search
def whenQuestion(sentenceArray):
    # search for time frame
    qDict = {} # Dict containing all useful information used
    timeFrames = {} # Future Dict for searching for time frames

    for word in sentenceArray:
        if word == 'born':
            qDict['timeQuestion'] = 'birth'
            subject = idObject(sentenceArray)
            # qDict['subject'] = subject
            stringToBe = subject[0]

            for word in range(len(subject)):
                if i != 0:
                    stringToBe += " " + word
            qDict['subject'] = stringToBe
            print qDict['subject']
            break

    # search for object

# Object identifier
# identifies object asked about in sentence
# input is full sentence
def idObject(sentenceArray):
    h = {}
    POS_tagged_sentence = nltk.pos_tag(sentenceArray)

    for index in range(len(POS_tagged_sentence)):
        if POS_tagged_sentence[index][1] == 'NNP':
            h[0] = sentenceArray[index]
            if POS_tagged_sentence[index+1][1] == 'NNP':
                h[1] = sentenceArray[index+1]
                if POS_tagged_sentence[index + 2][1] == 'NNP':
                    h[2] = sentenceArray[index+2]
                    break
                else:
                    break
            else:
                break
    return h
    # returns dict with object words
#     h = new hash table
# for i in array
#   if  i + 1 in h && i + 2 in h
#     return i, i+1, i+2
#   add i to h
# return no-match

def searchDemo(qString):
    # Parse string to identify question

    # getBirthday(getResource("Kanye West"))
    print getLabel("http://dbpedia.org/resource/Elvis_Presley")

def search(qString):
    # searchDemo(qString)
    parseQuestion(qString)
