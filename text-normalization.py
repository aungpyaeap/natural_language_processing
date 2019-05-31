# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# exercise
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words =  ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))
    
new_text =  """It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."""

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))


# exercise
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

raw = """DENNIS: Listen, strange women lying in ponds distributing swords is no basis for a system of government.  Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."""
#raw = """the quick brown fox jumps over the lazy dog"""

tokens = word_tokenize(raw)

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

print([porter.stem(t) for t in tokens])
print("\n")
print([lancaster.stem(t) for t in tokens])


import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

raw = """DENNIS: Listen, strange women lying in ponds distributing swords is no basis for a system of government.  Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."""
#raw = """the quick brown fox jumps over the lazy dog"""

tokens = word_tokenize(raw)

wnl = nltk.WordNetLemmatizer()
print([wnl.lemmatize(t) for t in tokens])
