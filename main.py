import Functions
from fuzzywuzzy import fuzz
from DataBase import STOCKS_INDEX_NAME
from DataBase import STOCKS_INDEX_SENTIMENT
import APIFunctions

print("[Welcome to the WSB Machine]")

DDTcomments = APIFunctions.getTopCommentsDDT()

for comment in DDTcomments[:80]:
    stock = Functions.getStock(comment.body, STOCKS_INDEX_NAME)
    if (stock != False):
        Functions.updateSentiment(comment.body, STOCKS_INDEX_SENTIMENT, stock)
    else:
        print("useless text: ", comment.body)

for index, item in enumerate(STOCKS_INDEX_SENTIMENT):
    if (STOCKS_INDEX_SENTIMENT[item] != 0):
        print("Stock: ", STOCKS_INDEX_NAME[item] , " Score:", STOCKS_INDEX_SENTIMENT[item])

"""
text = "Cognizant Technology Solutions is the worst stock of all time"
stock = Functions.getStock(text, STOCKS_INDEX_NAME)

Functions.updateSentiment(stock, STOCKS_INDEX_SENTIMENT, text)
"""

#Function to get the sentiment of a paragraph

