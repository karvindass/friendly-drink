import nltk # Used for natural language recognition
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)
from nltk.corpus import wordnet # Wordnet for finding synonyms
from nltk.tokenize import sent_tokenize, word_tokenize


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
