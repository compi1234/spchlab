from sklearn import metrics as skmetrics 
from sklearn.neural_network import MLPClassifier
import pyspch
from pyspch.stats import GMM
import pyspch.core as Spch

######   Classifier Utilities   #######################################
def train_GMM(X_train,y_train,classes=None,n_components=1,max_iter=10,Verbose=False,**kw_args):
    clf = GMM(classes=classes,n_components=n_components,max_iter=max_iter,**kw_args)                  
    clf.fit(X_train,y_train)
    ll, bic = clf.ll_and_bic(X_train,y_train)
    y_pred = clf.predict(X_train)
    acc_train = 100.0*skmetrics.accuracy_score(y_train, y_pred)
    if Verbose:
        print('Training Set:  Accuracy = %.2f%%' % (acc_train) )
        print('Training Set:  LL(per sample) = %.2f' % (ll) )
        print('Training Set:  BIC = %.2f' % (bic) )
    return(clf,acc_train) #,ll,bic))    

def train_MLP(X_train,y_train,classes=None,Verbose=False,
              learning_rate=0.005,hidden_layer_sizes=(256,),max_iter=500, early_stopping=True):   
    
    clf = MLPClassifier(solver='adam', 
                                    learning_rate_init=learning_rate_init,
                                    hidden_layer_sizes=hidden_layer_sizes,
                                    max_iter=max_iter, 
                                    early_stopping=early_stopping,
                                    alpha=1e-5, random_state=1, validation_fraction=0.1)
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_train)
    acc_train = 100.0*skmetrics.accuracy_score(y_train, y_pred)
    if(Verbose): print('Training Set:  Accuracy = %.2f%%' % (acc_train) )
    return(clf,acc_train)    


def test_clf(clf,X_test,y_test,Verbose=False,priors=None):
    try: # if classifier supports usage of priors
        if priors == 'uniform':
            priors = [1]*clf.n_classes
        elif priors == 'training':
            priors = None
        y_pred = clf.predict(X_test,priors=priors)
    except:
        y_pred = clf.predict(X_test)

    try:
        classes = clf.classes
    except:
        classes = clf.classes_
    n_classes = len(classes)
    
    acc_test = 100.0*skmetrics.accuracy_score(y_test, y_pred) 
    if(Verbose):
        print('Accuracy = %.2f%%'  % (acc_test) )
    conf_mat = skmetrics.confusion_matrix(y_test,y_pred,labels=classes)
    return(acc_test,conf_mat)

def test_GMM(clf_GMM,X_test,y_test,priors=None,norm=False,Verbose=False):
    try:
        if priors == 'uniform':
            priors = [1]*clf_GMM.n_classes
        elif priors == 'training':
            priors = None
    except:
        pass
    y_pred = clf_GMM.predict(X_test,priors=priors)
    acc_test = 100.0*skmetrics.accuracy_score(y_test, y_pred) 
    conf_mat = skmetrics.confusion_matrix(y_test,y_pred,labels=clf_GMM.classes)
    if Verbose:
        print('Test Set:      Accuracy = %.2f%%'  % (acc_test) )
        xx =  clf_GMM.n_classes/4. 
        Spch.plot_confusion_matrix(conf_mat,labels=clf_GMM.classes,norm=norm,figsize=(xx+3,xx+3),annot_kws={'fontsize':8})
    return(acc_test,conf_mat)