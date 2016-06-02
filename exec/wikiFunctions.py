import wikipedia

import nltk
from nltk.tokenize import word_tokenize

# Recommends a page name
def suggestPage(qString):
    return wikipedia.search(qString)[0]

# Gets RDF DBPedia Link for specific page
def getRDFLink(pageTitle):
    tokens = nltk.word_tokenize(pageTitle)
    qString = "http://dbpedia.org/resource/" + tokens[0]
    for i in range(1, len(tokens)):
        qString += "_" + tokens[i]

    return qString

# Gets RDF Link from provided topic (possibly incorrect entry)
def suggestRDFPage(topic):
    suggestedPage = suggestPage(topic)
    var = getRDFLink(suggestedPage)
    return var
