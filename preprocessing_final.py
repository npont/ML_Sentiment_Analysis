import pandas as pd
import numpy as np

import nltk
nltk.download('stopwords')


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
PATH='data/'
positive_words=open(PATH+'positive-words.txt').read().strip()
negative_words=open(PATH+'negative_words').read().strip()

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

def lemmatize_single(w):
    """
    DESCRIPTION: 
                Lemmatize a single word
    INPUT:  
            w: a word as a python string
    OUTPUT: 
            lemmatized word as a python string. In case the word cannot be lemmatized
            it will be returned in its first form.
    """
    try:
        a = lmt.lemmatize(w).lower()
        return a
    except Exception as e:
        return w
    
def stemming_single(word):
    """
    DESCRIPTION: 
                Apply stemming to a single word
    INPUT: 
            w: a word as a python string
    OUTPUT: 
            stemmed word as a python string. In case the word cannot be lemmatized
            it will be returned in its first form.
    """
    return lancaster_stemmer.stem(word) 

def stemming(tweet):
    """
    Function: 
            Stemming to all the words from a tweet one by one
    Input: 
            tweet as a python string
    Output: 
            stemmed tweet as a python string.
    """
    x = [stemming_single(t) for t in tweet.split()]
    return " ".join(x)

def lemmatize(tweet):
    """
    Function: 
            Lemmatize all words from a tweet one by one
    Input: 
            tweet: a tweet as a python string
    Output: 
            Lemmatized tweet as a python string.
    """
    x = [lemmatize_single(t) for t in tweet.split()]
    return " ".join(x)


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
        if (w in positive_words):
            w = ' positive ' + w
            tweet_emphasized.append(w) 
        elif (w in negative_words):
            w = ' negative '+ w
            tweet_emphasized.append(w)
        else: tweet_emphasized.append(w)
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
    return tweets.str.lower()


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
        tweets=tweets.str.replace(symbol, '<money>', regex=True)
    
    return tweets


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
        tweets=tweets.str.replace(punct, ' ', regex=True)

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
    tweets=tweets.str.replace('<user>', ' ', regex=True)
    tweets=tweets.str.replace('<url>', ' ', regex=True)
    tweets=tweets.str.replace('rt', ' ', regex=True)
    
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
    tweets = tweets.str.replace('im', 'i am', case=False)
    tweets = tweets.str.replace('&', 'and', regex=True)
    tweets = tweets.str.replace('btw', 'by the way', regex=True)
    tweets = tweets.str.replace('oc', 'of course', regex=True)
    tweets = tweets.str.replace('ily', 'i love you', regex=True)
    tweets = tweets.str.replace('ikr', 'i know right', regex=True)
    tweets = tweets.str.replace('idk', 'i don\'t know', regex=True)
    tweets = tweets.str.replace('dm', 'direct message', regex=True)
    tweets = tweets.str.replace('imo', 'in my opinion', regex=True)
    tweets = tweets.str.replace('nbd', 'no big deal', regex=True)
    tweets = tweets.str.replace('irl', 'in real life', regex=True)
    
    #expand contractions
    tweets = tweets.str.replace('n\'t', ' not', case=False)
    tweets = tweets.str.replace('i\'m', 'i am', case=False)
    tweets = tweets.str.replace('\'re', ' are', case=False)
    tweets = tweets.str.replace('it\'s', 'it is', case=False)
    tweets = tweets.str.replace('that\'s', 'that is', case=False)
    tweets = tweets.str.replace('\'ll', ' will', case=False)
    tweets = tweets.str.replace('\'l', ' will', case=False)
    tweets = tweets.str.replace('\'ve', ' have', case=False)
    tweets = tweets.str.replace('\'d', ' would', case=False)
    tweets = tweets.str.replace('he\'s', 'he is', case=False)
    tweets = tweets.str.replace('what\'s', 'what is', case=False)
    tweets = tweets.str.replace('who\'s', 'who is', case=False)
    tweets = tweets.str.replace('\'s', '', case=False)
    
    
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
    
    data_=convert_to_lowercase(data_)
    data_=filter_some_punctuation(data_)
    data_=filter_money(data_)
    #data_=filter_useless_words(data_)
    data_=expand_not(data_)

    t=[]
    for i in data_:
        i=emoji_transformation(i)
        i=lemmatize(i)
        i=stemming(i)
        i=emphasize(i)
        i=remove_stopwords(i)
        t.append(i)
    data_=t

    return data_