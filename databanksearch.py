import nltk # Used for Natural Language Processing
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)

import rdflib # Import for dbpedia usage
from rdflib import Graph, URIRef # Used to make dbpedia queries
from rdflib import RDFS # Used to get label name in dbpedia
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

