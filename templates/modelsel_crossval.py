#exec(open('templates\\modelsel_crossval.py').read())
# model evaluation by k-fold cross-validation
# TODO: stratified kfold
import subprocess as sp
import numpy as np
import pickle as pk
import sklearn.model_selection as ms
import sklearn.linear_model as sl

if __name__ == '__main__':
    sp.call('cls', shell = True)

    # load some data
    with open('.\\data\\pima.pkl', 'rb') as fl:
        df = pk.load(fl)

    # specify the x and y matrices
    ycols = ['class']
    xcols = list(set(df.columns) - set(ycols))
    X = df.loc[:, xcols].values
    y = np.ravel(df.loc[:, ycols].values)

    model = sl.LogisticRegression(max_iter = 1000)                          # select a model to use
    k = 10                                                                  # number of folds
    cvsplitter = ms.KFold(n_splits = k, shuffle = True, random_state = 0)   # cross-validation splitter
    accuracy = ms.cross_val_score(model, X, y, cv = cvsplitter)             # execute cross-validation on model
    print('Accuracy mean: {0:.4f}'.format(accuracy.mean()))
    print('Accuracy std: {0:.4f}'.format(accuracy.std()))