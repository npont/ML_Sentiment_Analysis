In this file we explain the organization of our project.
There are two notebooks:
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
    
There are python files containing useful functions:
- helpers is used to define functions used to load the data, create submission file for AlCrowd, average the word vectors, transform smileys of Y dataset into labels 1 and -1. 

The folder './data' contains 'positive-words.txt' and 'negative_words.txt' which are a list of words associated to the given sentiment and taken from reference [1] of the report. These are used in 'preprocessing' to create the 'emphasize' function. 