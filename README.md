## This project aims at classifying tweets as 'positive' or 'negative' according to the sentiment that is conferred. The labels correspond to 'smiling' or 'sad' smileys that have been removed.

### In this file we explain the organization of our project.

First, to run the files, you need to upload the twitter-datasets and store them into 'twitter-datasets/'. We used them locally on our computers but they are too heavy to be used on Github. 

### There are two notebooks:
- Simple_model: models done based on features representation with CountVectorizer, TF-IDF. The models are:
    . Naive Bayes Classifier (Bernoulli and Multinomial)
    . Linear SVC 
    . Bernoulli NB
    . Ridge Classifier
    . Nearest Centroid
    . SVM (Support vector machine)
    
- run_file : models trained on the GloVe matrix representation (weights matrix). The models are:
    . Logistic regression
    . SVM
    . SVC
    . Random Forest
    . Neural networks (keras and lstm)

- Sentiment Analysis
    
### There are python files containing useful functions:
- helpers is used to define functions used to load the data, create submission file for AlCrowd, average the word vectors, transform smileys of Y dataset into labels 1 and -1. 

The folder './data' contains 'positive-words.txt' and 'negative_words.txt' which are a list of words associated to the given sentiment and taken from reference [1] of the report. These are used in 'preprocessing' to create the 'emphasize' function. 

## How to run the files? 
We suggest the user to first go in 'simple models', and run cell by cell. It will give him a first insight into the models and accuracies. 
Then he should run the 'run_file' where he will actually realize a models training on the embeddings created through the GloVe method. 
Finally, he could run the sentiment analysis. However, this unsupervised method is quite different from the other models and gets quite bad accuracies. 
The other files are not to be used by the user. 
