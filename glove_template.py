#!/usr/bin/env python3
from scipy.sparse import *
import numpy as np
import pickle
import random


def main():
    print("loading cooccurrence matrix")
    with open('cooc.pkl', 'rb') as f:
        cooc = pickle.load(f)
    print("{} nonzero entries".format(cooc.nnz))

    nmax = 100
    print("using nmax =", nmax, ", cooc.max() =", cooc.max())

    print("initializing embeddings")
    embedding_dim = 20
    #weights:
    xs = np.random.normal(size=(cooc.shape[0], embedding_dim))
    ys = np.random.normal(size=(cooc.shape[1], embedding_dim))

    eta = 0.001
    alpha = 3 / 4

    epochs = 10
    loss_per_epoch=[]

    for epoch in range(epochs):
        print("epoch {}".format(epoch))
        for ix, jy, n in zip(cooc.row, cooc.col, cooc.data):
        
        # fill in your SGD code here, 
        # for the update resulting from co-occurence (i,j)
        
            #Computing grad_xi and grad_yj
            e_ij = np.dot(xs[ix, :], ys[jy, :]) - np.log(n)
            #weighting function defined by the GloVe authors:
            fM_ij = min(1.0, (n / nmax) ** alpha)
            grad_xi = 2 * fM_ij * e_ij * ys[jy, :]
            grad_yj = 2 * fM_ij * e_ij * xs[ix, :]

            #Computing intermediate loss for ix and jy:
            L += fM_ij * e_ij**2

            #Updating the weights
            xs[ix, :] -= eta * grad_xi
            ys[jy, :] -= eta * grad_yj
        
        loss_per_epoch.append(L)

    np.save('embeddings', xs)


if __name__ == '__main__':
    main()
