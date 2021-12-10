#!/usr/bin/env python
# coding: utf-8

# In[452]:


import pandas as pd
import numpy as np


# In[453]:


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


# In[454]:


def convert_and(tweets):
    """
    Function: converts & to and
    """
    
    return tweets.str.replace('&', 'and', regex=True)


# In[455]:


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


# In[456]:


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


# In[457]:


def filter_user(tweets):
    """
    Function: 
            Replaces the word '<user>' by an empty string.
    Input: 
            tweets 
    Output: 
            filtered <user>tweets
    """
    return tweets.str.replace('<user>', ' ', regex=True)


# In[458]:


def filter_url(tweets):
    """
    Function: 
            Replaces the word '<url>' by an empty string.
    Input: 
            tweets as strings
    Output: 
            filtered <url>tweets
    """
    return tweets.str.replace('<url>', ' ', regex=True)


# In[459]:


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


# In[460]:


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


# In[461]:


def pre_process(data_):
    """
    Function:
            call all the functions, to avoid having it in 'run_file'
    """
    
    data_=convert_to_lowercase(data_)
    data_=filter_some_punctuation(data_)
    data_=filter_money(data_)
    data_=filter_user(data_)
    data_=filter_url(data_)
    data_=expand_not(data_)
    
    
    #test filter emojis: 
    tweets=[":-] <3 :-p", "<3 :-p"]
    tweets_serie={'data': tweets}
    tweets_df=pd.DataFrame(tweets_serie)
    s=tweets_df.data
    t=[]
    for i in data_:
        i=emoji_transformation(i)
        t.append(i)
    data_=t

    return data_


# ## to check that the pre processing is working:

# In[462]:


check = ['COUCOU', "Coucou :-] <3", "c'est un <user>", "voici un <url>", "test punctuation ? . @", "ca coute 35 $ CHF", 
        "i'm don't"]
check_serie={'data': check}
check_df=pd.DataFrame(check_serie)
check_df.data=pre_process(check_df.data)
check_df


# In[463]:


#test filter emojis: 
tweets=[":-] <3 :-p"]
tweets_serie={'data': tweets}
tweets_df=pd.DataFrame(tweets_serie)
s=tweets_df.data
t=[]
for i in s:
    i=emoji_transformation(i)
    t.append(i)
tweets_df.data=t
tweets_df

