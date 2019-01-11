from comprehension import get_key_phrases
from analyzer import get_analyzer_mark
from scrapper import get_target_title
from comprehension import init 
from newsapi import get_news 
import sys
import logging

def get_score():   
    title = ((get_target_title(sys.argv[1], 2))[0] + ".").lower()
    comprehend_client = init(sys.argv[2], sys.argv[3])
    keyphrases = get_key_phrases(comprehend_client, title)
    newsapi_keys = []
    for phrase in keyphrases:
        newsapi_keys.append(phrase["Text"])
    trust = get_news(" ".join(newsapi_keys))

    ## not enough reliable news to compare
    if len(trust) < 3:
        print(-1)
        return -1

    score = 0 
    for trustnews in trust:
        score = score + get_analyzer_mark(comprehend_client, title, trustnews)
    score = round((score/len(trust)), 1)
    print(score)
    return score

get_score()