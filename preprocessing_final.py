import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords



## Initializations

## Initialize Stopwords
stopWords = stopwords.words("english")
## Initialize Stemmer
lancaster_stemmer = LancasterStemmer()
## Initialize Lemmatizer
lmt = WordNetLemmatizer()

## Load positive and negative words
## Load positive and negative words
PATH='data/'
positive_words=open(PATH+'positive-words.txt').read().strip()
positive_words=positive_words.split()
negative_words=open(PATH+'negative_words.txt').read().strip()
negative_words=negative_words.split()

def remove_stopwords(tweet):
    """
    Function: 
            filters stopwords from a tweet
    Input:
            tweet as a python string
    Output: 
            a stopword-filtered tweet
    """
    tokens = tweet.split()
    for word in tokens:
        if word in stopWords:
            tokens.remove(word)
    return ' '.join(tokens)

def filter_money(tweets):
    """
    Function:
            assign tag to money symbols
    Input:
            tweets as python
    Output:
            money filtered tweets
    """
    
    money_symbols=['$', 'chf', '€']
    
    for symbol in money_symbols:
        tweets=tweets.replace(symbol, '<money>')
    
    return tweets

def emphasize(tweet):
    """
    Function:
            adds 'positive' or 'negative' to words of tweet if they are in {Positive/Negative}_words 
    Input:
            tweet as python string
    Output: 
            tweet with words associated to 'positive' or 'negative'
    """
    tweet_emphasized=[]
    for w in tweet.split():
        if (positive_words.count(w) > 0):
            w_pos = ' positive ' + w
            tweet_emphasized.append(w_pos) 
        elif (negative_words.count(w) > 0):
            w_neg = ' negative '+ w
            tweet_emphasized.append(w_neg)
        else:
            tweet_emphasized.append(w)
    return (" ".join(tweet_emphasized)).strip()


def convert_to_lowercase(tweets):
    """
    Function: 
             Converts tweets into lowercases
    Input: 
            tweets as strings
    Output: 
            tweets as lowercases 
    """
    return tweets.lower()


def filter_some_punctuation(tweets):
    """
    Function:
            deletes some useless punctuation
    Input:
            tweets as strings
    Output:
            tweets with filtered punctuation
    """
    
    useless_punct=['.', '?', '@', ',']
    
    for punct in useless_punct:
        tweets=tweets.replace(punct, ' ')

    return tweets

def filter_useless_words(tweets):
    """
    Function: 
            Replaces useless words by an empty string.
    Input: 
            tweets as strings
    Output: 
            filtered useless_words-tweets
    """
    tweets=tweets.replace('<user>', ' ')
    tweets=tweets.replace('<url>', ' ')
    tweets=tweets.replace('rt', ' ')
    
    return tweets

def expand_not(tweets):
    """
    Function: 
            Replaces contractions of words into the formal form. In other terms, it expands the contractions. 
            For e.g, "i'm" will be expanded to "i am".
    Input: 
            tweets as strings
    Output:
            tweets with contractions expanded
    """
    
    
    #abreviations
    tweets = tweets.replace('im', 'i am')
    tweets = tweets.replace('&', 'and')
    tweets = tweets.replace('btw', 'by the way')
    tweets = tweets.replace('oc', 'of course')
    tweets = tweets.replace('ily', 'i love you')
    tweets = tweets.replace('ikr', 'i know right')
    tweets = tweets.replace('idk', 'i don\'t know')
    tweets = tweets.replace('dm', 'direct message')
    tweets = tweets.replace('nbd', 'no big deal')
    tweets = tweets.replace('irl', 'in real life')
    
        #expand contractions
    tweets = tweets.replace('n\'t', ' not')
    tweets = tweets.replace('don\'t', ' do not')
    tweets = tweets.replace('i\'m', 'i am')
    tweets = tweets.replace('\'re', ' are')
    tweets = tweets.replace('it\'s', 'it is')
    tweets = tweets.replace('that\'s', 'that is')
    tweets = tweets.replace('\'ll', ' will')
    tweets = tweets.replace('\'l', ' will')
    tweets = tweets.replace('\'ve', ' have')
    tweets = tweets.replace('\'d', ' would')
    tweets = tweets.replace('he\'s', 'he is')
    tweets = tweets.replace('what\'s', 'what is')
    tweets = tweets.replace('who\'s', 'who is')
    tweets = tweets.replace('\'s', '')

    return tweets


def emoji_transformation(tweet):
    """
    Function: 
            replaces emoticons/smileys by tags. For e.g, <3 will be replaced by <heart>
    Input: 
            tweet as string
    Output: 
            transformed tweet as string
    """

    #Possible emoticons_Construction:
    hearts = ["<3", "♥"]
    eyes = ["8",":","=",";"]
    nose = ["'","`","-",r"\\"]
    smiley = []
    sadfaces = []
    neutralfaces = []
    funnyfaces = []

    for e in eyes:
        for n in nose:
            for s in ["\)", "d", "]", "}"]:
                smiley.append(e+n+s)
                smiley.append(e+s)
            for s in ["\(", "\[", "{"]:
                sadfaces.append(e+n+s)
                sadfaces.append(e+s)
            for s in ["\|", "\/", r"\\"]:
                neutralfaces.append(e+n+s)
                neutralfaces.append(e+s)
            #emoji in other sense (e.g, :-) can also be found as (-: )
            for s in ["\(", "\[", "{"]:
                smiley.append(s+n+e)
                smiley.append(s+e)
            for s in ["\)", "\]", "}"]:
                sadfaces.append(s+n+e)
                sadfaces.append(s+e)
            for s in ["\|", "\/", r"\\"]:
                neutralfaces.append(s+n+e)
                neutralfaces.append(s+e) 
            funnyfaces.append(e+n+"p")
            funnyfaces.append(e+"p")

    smiley = set(smiley)
    sadfaces = set(sadfaces)
    neutralfaces = set(neutralfaces)
    funnyfaces = set(funnyfaces)
    
    t = []
    for w in tweet.split():
        if(w in hearts):
            t.append("<heart>")
        elif(w in smiley):
            t.append("<smile>")
        elif(w in funnyfaces):
            t.append("<funnyface>")
        elif(w in neutralfaces):
            t.append("<neutralface>")
        elif(w in sadfaces):
            t.append("<sadface>")
        else:
            t.append(w)
    return (" ".join(t)).strip()


def pre_process(data_):
    """
    Function:
            call all the functions, to avoid having it in 'run_file'
    """

    t=[]
    for i in data_:
        i=convert_to_lowercase(i)
        i=filter_money(i)
        i=filter_useless_words(i)
        i=filter_some_punctuation(i)
        i=expand_not(i)
        i=emoji_transformation(i)
        i=remove_stopwords(i)
        i=emphasize(i)
        
        t.append(i)
    data_=t

    return data_