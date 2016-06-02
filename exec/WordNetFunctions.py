import nltk # Used for natural language recoginition
from nltk.corpus import wordnet # Wordnet for finding synonyms

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
