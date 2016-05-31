from rdflib import Graph, URIRef # Used to make dbpedia queries
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)

    g=rdflib.Graph()
    g.load('http://dbpedia.org/resource/Semantic_Web')

    for s,p,o in g:
        print s,p,o
