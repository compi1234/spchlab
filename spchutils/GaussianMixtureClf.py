# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:41:29 2019

@author: compi

"""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
#from scipy.special import logsumexp

class GaussianMixtureClf(BaseEstimator, ClassifierMixin):
    """ Gaussian Mixture Model based Classifier
    
    Attributes
    ----------
    
    n_classes :    int,
        number of classes
    n_components : int,
        number of components in each Mixture
    max_iter :     int, 
        maximum number of iterations in GMM updates
    tol :          float64,
        tolerance  for converging GaussianMixture
    
    class_prior_ : array, shape (n_classes,)
        probability of each class.
    class_count_ : array, shape (n_classes,)
        number of training samples observed in each class.   
        
    
    
    """   
    def __init__(self, n_components=1 ,classes=[0,1], max_iter=10, tol=1.e-3):
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol

        self.data_range_ = None

        self.classes = classes
        self.n_components=n_components
        self.n_classes = len(self.classes)
        self.class_count_ = np.zeros(self.n_classes,dtype='float64')
        self.class_prior_ = np.ones(self.n_classes,dtype='float64')/float(self.n_classes)
        
        self.gmm = [GaussianMixture(max_iter=self.max_iter,tol=self.tol,random_state=1,n_components=self.n_components, 
                        covariance_type='diag',init_params='kmeans') for k in range(0,self.n_classes)]   


        
    def _validate_params(self):
        if self.n_classes < 2:
            raise ValueError("Minimum Number of Classes is 2")
        if self.n_classes != len(self.gmm):
            raise ValueError("Initialized GMM shape(%d,_) does not match n_classes(%d) "
                % (len(self.gmm), self.n_classes) )
    
        
    def fit(self, X, y):
        """Fit GMM with EM for each class.
    
        Parameters
        ----------
        X : {array-like}, shape (n_samples, n_features)
            Training data
    
        y : numpy array, shape (n_samples,)
            Target values
        
        
        Returns
        -------
        self : returns an instance of self.
        """

        for k in range(0,self.n_classes):
            self.gmm[k]._check_parameters(X)

        classes = np.unique(y)
        if(len(classes) > len(self.gmm)):
            raise ValueError("More classes in data than in allocated GMMs")

        for k in range(0,self.n_classes) :
            selection = (y== self.classes[k])
            self.gmm[k].fit(X[selection,: ])
            self.class_count_[k] = np.sum(selection)
#            print("Model for class: ",self.gmm[k].means_,np.sqrt(self.gmm[k].covariances_))        
              
        # keep the counts in the model for adaptation and incremental training purposes
        # keep the datarange for summary / plotting utilities
        self.class_prior_ = self.class_count_ / len(y)
        self.data_range_ = np.vstack((np.min(X,axis=0),np.max(X,axis=0)))
        
    def predict_log_prob(self,X):
        """ Likelihoods of  X  for each class
        
            Returns
            -------
            array, shape (n_samples, n_classes)
                Predicted likelihoods per class
                
            array, shape (n_samples,)
                Total Likelihood per sample
        """
        Xprob = np.ndarray(dtype='float64',shape=(X.shape[0],self.n_classes))
        for k in range(0,self.n_classes):
            Xprob[:,k]= self.gmm[k].score_samples(X)      
        return Xprob

    def predict_prob(self,X):
        """ Log-Probability estimates (likelihoods) per class
        """
        return np.exp(self.predict_log_prob(X))

        

    def predict_proba(self, X, priors = None):
        """ 
        Computes the class probabilities (posteriors) given the samples
        You can override the priors derived during training
        """
        
        if priors == None:
            priors = self.class_prior_
            
        if (len(priors) != self.n_classes):
            raise ValueError("Dimensions of priors do not match number of classes")
            
        likelihoods = self.predict_prob(X)
        nsamples = X.shape[0]
        total_likelihood = np.zeros(nsamples)
        posteriors = np.zeros((nsamples,self.n_classes))
        for k in range(0,self.n_classes):
            likelihoods[:,k] =  priors[k]*likelihoods[:,k]
            total_likelihood += likelihoods[:,k]
        for k in range(0,self.n_classes):
            posteriors[:,k] = np.divide(likelihoods[:,k],total_likelihood)
                    
        return(posteriors)

    
    def predict(self, X,priors=None):
        indx = self.predict_proba(X,priors=priors).argmax(axis=1)
        return( [self.classes[k] for k in indx ] )

            
    def print(self):
        """ print the model """
        for k in range(0,self.n_classes):
            print("Class[%d] (%s) with prior=%.3f" % (k,self.classes[k],self.class_prior_[k]))
            print("-----------------------------------")


            if  self.gmm[k].means_.shape[1] == 1 :
                df = pd.DataFrame(data={'weights':self.gmm[k].weights_.reshape(-1), 
                                    'mean':self.gmm[k].means_.reshape(-1), 
                                    'std_dev':np.sqrt(self.gmm[k].covariances_).reshape(-1)})
                print(df)
            else:
               print(self.gmm[k].weights_,self.gmm[k].means_,
                 np.sqrt(self.gmm[k].covariances_))        
    
    def plot_prob(self):
        """ 
        plot the likelihood distributions 
        ... untested 
        """
        if( self.data_range_ == None ):
            raise ValueError("No data_range_ given for the plots")
        npts = 100
        ndim = len(self.data_range_,axis=1)
        if(ndim>2):
             raise ValueError("plot_prob only for 1-D or 2-D data")
        elif(ndim==2):
            x = np.linspace(self.data_range_[0,0],self.data_range_[1,0],num=npts)
            y = np.linspace(self.data_range_[0,1],self.data_range_[1,1],num=npts)
            xx,yy = np.meshgrid(x,y, sparse=True)
            z = self.predict_prob(np.vstack(xx,yy))
            h = plt.contourf(x,y,z)
            plt.show()
        else:
            x = np.linspace(self.data_range_[0,0],self.data_range_[1,0],num=npts)
            z = self.predict(np.vstack(x))
            h = plt.plot(x,z)
            plt.show()
