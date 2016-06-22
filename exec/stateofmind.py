import nltk # Used for natural language recognition
from nltk.stem import WordNetLemmatizer # Used to lemmatize (find root word)
from nltk.corpus import wordnet # Wordnet for finding synonyms
from nltk.tokenize import sent_tokenize, word_tokenize

from findsynonyms import findSynonyms

def fnchk(sentence):
    stom=0
    fnSynonyms= findSynonyms("fine")+ findSynonyms("good")+findSynonyms("happy")
    ntSynonyms= findSynonyms("not")
    sdSynonyms= findSynonyms("sad")+findSynonyms("sick")+findSynonyms("bad")

    for i in range (0, (len(sentence))):
        ki=0
        if (len(sentence))==1:
            li=0
            for syns in fnSynonyms:
                li=1
                if sentence[i][0].lower()==syns:
                    return True
                    break
                if li==0:
                    for syns in sdSynonyms:
                        if sentence[i][0].lower()==syns:
                            return False
                            break

        elif sentence[i][1]=='JJ':
            for syns in fnSynonyms:
                if syns == sentence[i][0].lower():
                    ki=1
                    if i==0:
                        return True
                    else:
                        for k in range (0, (i)):
                            if (sentence[k][0].lower()=="not" or sentence[k][0].lower()=="non"):
                                return False
                            else:
                                continue
                        return True
                    break
            if ki==0:
                for syns in sdSynonyms:
                    if syns == sentence[i][0]:
                        if i==0:
                            return False
                        else:
                            for k in range (0, (i)):
                                if (sentence[k][0].lower()=="not" or sentence[k][0].lower()=="non"):
                                    return True
                                else:
                                    continue
                            return False
                        break
