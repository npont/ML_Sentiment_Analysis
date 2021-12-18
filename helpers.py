{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}

import csv
import pandas as pd

def create_csv_submission(ids, y_pred, name):
    """
    Creates an output file in .csv format for submission to Kaggle or AIcrowd
    Arguments: ids (event ids associated with each prediction)
               y_pred (predicted class labels)
               name (string name of .csv output file to be created)
    """
    with open(name, 'w') as csvfile:
        fieldnames = ['Id', 'Prediction']
        writer = csv.DictWriter(csvfile, delimiter=",", fieldnames=fieldnames)
        writer.writeheader()
        for r1, r2 in zip(ids, y_pred):
            if (r2==':)'):
                r2=1
                writer.writerow({'Id':int(r1),'Prediction':r2})
            if(r2==':('):
                r2=-1
                writer.writerow({'Id':int(r1),'Prediction':r2})
                
                
def load_data():
    with open('twitter-datasets/train_pos.txt') as f:
        pos = f.readlines()
    
    with open('twitter-datasets/train_neg.txt') as f:
        neg = f.readlines()
        
    train=pos+neg
    train_target=[':)']*len(pos)+[':(']*len(neg)
    full_train={'data':train,'target':train_target}
    full_train=pd.DataFrame(full_train)
    
    return full_train


def init_target(i):
    'convert smiley to 1/-1'
    if i == ':)':
        i = 1
    elif i== ':(':
        i = -1
    return i

def transform_smiley(Y_train):
    
    Y_train_init=[]

    for i in range (len(Y_train)):
        Y_train_init.append(init_target(Y_train[i]))
        
    return Y_train_init

def average_word_vectors(tweets ,word_embedding):
    
    error = 0
    avg_word_vectors = np.zeros((len(tweets), word_embedding.shape[1] ))
    for i, tweet in enumerate(tweets):
        
        split_tweet = tweet.split()
        nb_words = 0
        
        for word in split_tweet:
            try:
                avg_word_vectors[i] += word_embedding.loc[word].to_numpy()
                nb_words += 1

            except KeyError: 
                continue
        if (nb_words != 0):
            avg_word_vectors[i] /= nb_words
        
    return avg_word_vectors