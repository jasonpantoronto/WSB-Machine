from textblob import TextBlob
from fuzzywuzzy import fuzz
"""
Some notes:
Use fuzz.token_set_ratio(text 1, text 2) to see if there is a match
.token_set_ratio is case insensitive
.ratio is case is case sensitive
"""

#Args = the paragraph to analyse
def getSentimentParagraph(text):
    sentiment = 0
    numOfSentences = 0
    blob = TextBlob(text)
    for sentence in blob.sentences:
        numOfSentences += 1
        sentiment += sentence.sentiment.polarity
    return sentiment/numOfSentences

#Args = the paragraph to analyse, hashmap of the stock symbol and full names
#Loops through every single item in the dictionary. If there is a match to a symbol or the item held by the symbol (full name of stock), then the symbol will be returned. False if no match.
def getStock(text, INDEX_DIC):
    for index, item in enumerate(INDEX_DIC):
        if (fuzz.token_set_ratio(item, text) == 100 or fuzz.token_set_ratio(INDEX_DIC[item], text) == 100):
            return item
    return False

#Args = the paragraph to analyse, hashmap of the scores of sentiment, stock
#Upon call -> getSentimentParagraph(). Returns the INDEX that has been updated.
def updateSentiment(text, INDEX_SENTIMENT, item):
    sentiment = getSentimentParagraph(text)
    INDEX_SENTIMENT[item] += sentiment
    return INDEX_SENTIMENT