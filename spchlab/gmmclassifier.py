# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:41:29 2019

@author: compi
"""

import numpy as np
from sklearn.mixture import GaussianMixture


""" Classification using Gaussian Mixture Models """
class gmmclassifier():
    """ A Gaussian Mixture Model Classifier
    Parameters
    
    Assumptions:
        there is an implicit assumption that classes will be labeled 0 ... n_classes - 1   
    """
    
    def __init__(self,max_iter=10, tol=1.e-3, shuffle=True, n_g=1, n_classes=None,
             warm_start= False,gmm_init =None):

        self.max_iter=max_iter
        self.tol=tol
        self.shuffle=shuffle
        self.warm_start = warm_start
        
        if not self.warm_start:
            self.n_g=n_g
            self.n_classes = n_classes
            self.gmm = [GaussianMixture(max_iter=self.max_iter,tol=tol,random_state=1,n_components=self.n_g, 
                        covariance_type='diag',init_params='kmeans') for k in range(0,self.n_classes)]   
        else:
            self.gmm = gmm_init
        
#        if class id's aren't given, number thme 0 ... n_classes - 1
#        if classes == None:
#            for k in range(0,self.n_classes):
#                classes[k] = k;
        
#        self._validate_params()
    

        
    def _validate_params(self):
        if self.n_classes < 2:
            raise ValueError("Minimum Number of Classes is 2")
        if self.n_classes != len(self.gmm):
            raise ValueError("Initialized GMM shape(%d,_) does not match n_classes(%d) "
                % (len(self.gmm), self.n_classes) )
    

    def fit(self,X,y,method='ML'):
        """Fit linear model with Stochastic Gradient Descent.
    
        Parameters
        ----------
        X : {array-like}, shape (n_samples, n_features)
            Training data
    
        y : numpy array, shape (n_samples,)
            Target values
        
        method :'ML' (maximum likelihood)
        
        Returns
        -------
        self : returns an instance of self.
        """

        for k in range(0,self.n_classes):
            self.gmm[k]._check_parameters(X)
        
        n_samples, n_features = X.shape
        classes = np.unique(y)
        
    
        if(len(classes) > len(self.gmm)):
            raise ValueError("More classes in data than in allocated GMMs")

        for k in range(0,self.n_classes) :
            ksel = [y[i] == classes[k] for i in range(n_samples)]
            XX = X[ksel,:]
            print(XX.shape)
            self.gmm[k].fit(X[ksel],y[ksel])
#            print("Model for class: ",self.gmm[k].means_,np.sqrt(self.gmm[k].covariances_))
        
        
    def predict(self,X):
            """Predict using the linear model
    
            Parameters
            ----------
            X : {array-like}, shape (n_samples, n_features)
    
            Returns
            -------
            array, shape (n_samples,)
               Predicted target values per element in X.
        
        """
        
    def predict_prob(self,X):
        """ Posterior Probability estimates per class
        
            Returns
            -------
            array, shape (n_samples, n_classes)
                Predicted likelihoods per class
                
            array, shape (n_samples,)
                Total Likelihood per sample
        """
        Xprob = np.ndarray(dtype='float64',shape=(X.shape[0],self.n_classes))
        Tprob = np.zeros(dtype='float64',shape=(X.shape[0],))
        for k in range(0,self.n_classes):
            Xprob[:,k]= np.exp(self.gmm[k].score_samples(X))
            Tprob += Xprob[:,k]
            
        return Xprob, Tprob
            
    def print(self):
        for k in range(0,self.n_classes):
            print(self.gmm[k].weights_,self.gmm[k].means_,
                  np.sqrt(self.gmm[k].covariances_))            