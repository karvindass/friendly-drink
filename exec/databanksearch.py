import nltk # Used for Natural Language Processing
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)
from nltk.tokenize import sent_tokenize, word_tokenize # Used to sentence and word tokenize

import rdflib # Import for dbpedia usage
from rdflib import Graph, URIRef # Used to make dbpedia queries
from rdflib import RDFS # Used to get label name in dbpedia

import wikiFunctions as wiki # import functions needed for dbpedia queries

# Get Birthday of resource
def getBirthday(rdfFile):
    g = Graph() # Creates graph object
    g.parse(rdfFile) # Parses through rdfFile

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")): # finds subjects and objects with predicate of birthDate
        return stmt[1] # Returns first value found

# Get Deathday of resource
def getDeathday(rdfFile):
    g = Graph() # Creates graph object
    g.parse(rdfFile)

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/deathDate")): #finds subjects and objects with predicate of deathDate
        return stmt[1]

    # Control flow when no deathDate found
    return "not found, are you sure they have died?" # Returned if deathDate not found

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
def parseQuestion(fullString):
    sentenceArray = sent_tokenize(fullString)

    for sentence in sentenceArray:
        qIndex = qQuestion(sentence) # return index of question type
        if qIndex == 3: # 'When' question
            whenQuestion(word_tokenize(sentence))

# Identifies what kind of question it is asking  (Who/What/Where/When/What/How)
def qQuestion(querySentence):
    wordsInSentence = word_tokenize(querySentence)
    qWords = ['who','what','where','when','what','how']

    for word in wordsInSentence:
        if word in qWords:
            # Proceed if question word is found
            return qWords.index(word)

# When question
# Carried out when 'when' is identified as the question word
def whenQuestion(sentenceArray):
    # search for time frame
    qDict = {'question': 'when'} # Dict containing all useful information used
    timeFrames = {} # Future Dict for searching for time frames
    for word in sentenceArray:
        if word == 'born':
            # Proceed if asking about birthday
            qDict['timeQuestion'] = 'birth'
            subject = idObject(sentenceArray)
            stringToBe = subject[0]

            for word in range(len(subject)):
                if word != 0:
                    stringToBe += " " + subject[word]
            qDict['subject'] = stringToBe
            break

        elif word == 'die':
            qDict['timeQuestion'] = 'death'
            subject = idObject(sentenceArray)
            stringToBe = subject[0]

            for word in range(len(subject)):
                if word != 0:
                    stringToBe += " " + subject[word]
            qDict['subject'] = stringToBe
            break

    RDFlink = wiki.suggestRDFPage(qDict['subject'])
    if qDict['timeQuestion'] == 'birth':
        timeValue = getBirthday(RDFlink) # get's the value requested, in birth case - date
        print ("%s was born on %s" % (qDict['subject'].title(), timeValue))
    elif qDict['timeQuestion'] == 'death':
        timeValue = getDeathday(RDFlink)
        print ("%s died on %s" % (qDict['subject'].title(), timeValue))



# Object identifier
# identifies object asked about in sentence
# input is full sentence
def idObject(sentenceArray):
    h = {}
    # Let's assume for ease of use that only the phrase 'When was X Y born?'
    h[0] = sentenceArray[2]
    h[1] = sentenceArray[3]
    # POS_tagged_sentence = nltk.pos_tag(sentenceArray)
    # print POS_tagged_sentence
    # for index in range(len(POS_tagged_sentence)-1):
    #     print index + " " + POS_tagged_sentence[index][1]
    #     if POS_tagged_sentence[index][1] == 'NNP':
    #         h[0] = sentenceArray[index]
    #         if POS_tagged_sentence[index+1][1] == 'NNP':
    #             h[1] = sentenceArray[index+1]
    #             if POS_tagged_sentence[index + 2][1] == 'NNP':
    #                 h[2] = sentenceArray[index+2]
    #                 break
            #     else:
            #         break
            # else:
            #     break
    return h


def searchDemo(qString):
    print getLabel("http://dbpedia.org/resource/Elvis_Presley")

def search(qString):
    parseQuestion(qString)
