# LAB07:  Dynamic Time Warping

## Background

DTW finds a sequence distance between two sequences of vector data 
$$ 
X_{i=1:N} \text{  and  } Y_{j=1:M}  
$$

The **sequence distance** is the minimum of the cummulative distances among all possible alignment paths
$$
(X_{i(s)},Y_{j(s)} ) \text{  for } s=1 ... L 
$$

whereas the cummulative distance along a given path is defined as:   
$$
\sum_s  D_l\left(X_{i(s)}, Y_{j(s)}\right) + D_t\left(\it{trans}\right) 
$$   
with:  $ trans = \left( i(s)-i(s-1),  j(s)-j(s-1) \right) $

+ with $D_l(X,Y)$ denoting a *local distance metric* that measures distance between 2 feature vectors
+ with $D_t(..)$ denoting a *transition cost* depending on the transition that was taken
+ boundary constraints:
    + if you need $\{X\}$ to be a match for $\{Y\}$ then the alignment should start in the origin $(1,1)$ and end in $(N,M)$
    + if you want to find the best possible subsequence match of $\{X\}$ in $\{Y\}$, then any starting point (1,j_1) and any endig point (N,j_L) is acceptable  
+ certain transition constraints are generic:
    +  $i$ and $j$ need to *progress* in time, i.e. $i(s+1) >= i(s)$
    + the diagonal transition (+1,+1) is natural and by default alwasys included in the list of allowed transitions
+ certain transition constraints are specific to the applied transition model:
    + In a Levenshtein model for string matching
        * DIAGONAL: (+1,+1), INSERTION: (+1,0), DELETION: (0,+1)
        * For INSERTION and DELETION only a fixed transition cost is added
        * For DIAGONAL transitions the local distance cost is added 
    + In (vanilla) DTW 
        * the basic transitions are: (+1,+1), (+1,0), (0,+1)
        * a local distance metric is defined, allowing to built the local distance matrix $D_l\left(X_i, Y_j\right)$
        * either no transition costs are taken into account, or a transition penalty is added to the non diagonal transitions
     + In Symmetric Itakura
         * the possible transitions are: (+1,+1), (+2,+1), (+1,+2)
         * a local distance matrix is built as above
         * the long moves may be seen as double transitions, therefore the local distances 'along the way' should be accumulated; alternatively a multiplicative cost (eg. 2) can be implemented
         
The two DTW models described above, can be visualized as here:
[dtw_constraints](dtw_constraints.png)



## Exercises



#### String Matching

*notebook:* [Levenshtein1.ipynb](Levenshtein1.ipynb)

- Exercise 1: elementary string matching
- Exercise 2: character or word matching for sentences
- Exercise 3: error rate computations for speech recognition


#### DTW on 1D data

*notebook:* [dtw1.ipynb](dtw1.ipynb)

- Exercise 1: DTW on 1-dimensional feature vector sequence
- Exercise 2: Using different warping constraints


#### DTW on speech data

... coming soon ...


