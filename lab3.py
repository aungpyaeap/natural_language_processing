# sentence segmentation
from nltk.tokenize import sent_tokenize, word_tokenize
sampleText = "This is a programThis programme is designed to provide students with knowledge and applied skills in data science, big data analytics and business intelligence. It aims to develop analytical and investigative knowledge and skills using data science tools and techniques, and to enhance data science knowledge and critical interpretation skills. Students will understand the impact of data science upon modern processes and businesses, be able to identify, and implement specific tools, practices, features and techniques to enhance the analysis of data."
sentences = sent_tokenize(sampleText)
print("There are ", len(sentences), "sentences in this text\n")
counter=0
for sent in sentences:
    counter+=1
    print(counter, ".", sent, "\n")
    
print("AA")


# word tokenination
from nltk.tokenize import sent_tokenize, word_tokenize
sampleText = "This programme is designed to provide students with knowledge and applied skills in data science, big data analytics and business intelligence. It aims to develop analytical and investigative knowledge and skills using data science tools and techniques, and to enhance data science knowledge and critical interpretation skills. Students will understand the impact of data science upon modern processes and businesses, be able to identify, and implement specific tools, practices, features and techniques to enhance the analysis of data."

Tokens = word_tokenize(sampleText)

print("There are ", len(Tokens), "tokens in this text\n")

counter = 0
for w in Tokens:
    counter+=1
    print(counter,".",w)

Tokenstext = nltk.Text(Tokens)
print(Tokenstext[1:len(Tokenstext)])


# accessing text from web
from urllib.request import urlopen
from nltk.tokenize import sent_tokenize, word_tokenize
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
sampletext = urlopen(url).read().decode('utf8')
len(sampletext)


# dealing with HTML
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
sampletext =  urlopen(url).read().decode('utf8')
from bs4 import BeautifulSoup
texttoken = BeautifulSoup(sampletext).getText()


# reading local files
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

filehandler = open('sample.txt')
sampletext = filehandler.read()

tokens = word_tokenize(sampletext)
print("There are", len(tokens), "words in the text\n")

stoptokens = stopwords.words("english")
filteredtokens = []

for w in tokens:
    if w not in stoptokens:
        filteredtokens.append(w)
    
print("There are ", len(filteredtokens), "words in this text after removing stop words\n")
print(filteredtokens)

