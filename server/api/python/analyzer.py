from comprehension import init, get_entities, get_key_phrases, get_sentiment

def get_analyzer_mark(comprehend_client, mainnews, trustnews):
    sentiment = sentiment_mark(comprehend_client, mainnews, trustnews)
    return ((9*keyphrases_mark(comprehend_client, mainnews, trustnews)) + (1*entities_mark(comprehend_client, mainnews, trustnews))) * sentiment

def keyphrases_mark(compr, title1, title2):
    value = 0
    key_phrases1 = get_key_phrases(compr, title1)
    key_phrases2 = get_key_phrases(compr, title2)
    if len(key_phrases1) == 0:
        return 1
    for phrase1 in key_phrases1:
        for phrase2 in key_phrases2:
            for words1 in phrase1.get('Text').split(" "):
                for words2 in phrase2.get('Text').split(" "):
                    if words1 == words2:
                        value += 1/len(key_phrases1)
                        words1= ""
                        break
                if words1 == "": 
                    phrase1=None
                    break
            if phrase1 is None:
                break
    return value

def entities_mark(compr, title1, title2):
    value = 0
    entity_list1 = get_entities(compr, title1)
    entity_list2 = get_entities(compr, title2)
    if len(entity_list1) == 0 or len(entity_list2) == 0:
        return 1

    for entity1 in entity_list1:
        for entity2 in entity_list2:
            if entity1.get('Text') == entity2.get('Text'):
                value += 1/len(entity_list2)
                break
            elif entity1.get('Type') == entity2.get('Type') and '%.3f'%(entity2.get('Score')) <= '%.3f'%(entity1.get('Score')):
                value += 0.9/len(entity_list2)
                break
    return value

def sentiment_mark(compr, title1, title2):
    sentiment_list1 = get_sentiment(compr, title1)
    sentiment_list2 = get_sentiment(compr, title2)

    if sentiment_list1[0] == 'MIXED':
        return 1-abs((sentiment_list2[1].get('Positive') - sentiment_list1[1].get('Positive'))/3 +
                        (sentiment_list2[1].get('Negative') - sentiment_list1[1].get('Negative'))/3 +
                        (sentiment_list2[1].get('Neutral') - sentiment_list1[1].get('Neutral'))/3)
    elif sentiment_list1[0] == sentiment_list2[0]:
        return 1-abs((sentiment_list2[1].get(sentiment_list2[0]) - sentiment_list1[1].get(sentiment_list2[0])))
    else:
        return abs((sentiment_list2[1].get(sentiment_list2[0]) - (1 - sentiment_list1[1].get(sentiment_list2[0]))))
