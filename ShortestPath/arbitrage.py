'''Here we present a fun application of the 
Bellman-Ford algorithm to determine, given a 
table R = [r_ij] of currency exchange rates,
where r_ij is the exchange rate from currency
i to currency j, if there exists an arbitrage 
oppurtunity.  All of these exchange rates are
assumed to be non-negative.  

Namely, does there exists a cycle where the
product of the weights of the cycle is greater
than 1. 

Tricks: 
1) This is equivalent to the case where 
   the product of the reciprocals of the 
   weights is less than 1.0.  
2) This is equivalent to the sum of the logs 
   of the weights being greater than 0.0!

So it suffices on the log-reciprocal graph
to check for a negative cycle.  Bellman-Ford
can also be modified to return a negative cycle
when it exists.  

(Note: In general, the Longest Path problem
is NP-complete, so there is no (P=?NP) reduction
from longest paths to shortest paths.  Here we 
have a trick since we are weighting paths by 
the products of the edge weights as opposed to 
the sums.)
'''

import math


def arbitrage(R):
    '''Given a currency exchange matrix, 
    returns if there is an arbitrage 
    opportunity.  
    '''

    V = len(R)
    INF = float("inf")
    d = {i: INF for i in range(V)}
    d[0] = 0  # Arbitrary source.

    # Can do this implicitly but let's
    # save some redundant computation.
    R_transformed = [[math.log(1.0 / R[i][j])
                     for j in range(V)]
                     for i in range(V)]

    for _ in range(V - 1):

        # Complete graph so BF with adjacency matrix.
        for i in range(V):
            for j in range(V):
                if i == j:
                    continue
                d[j] = min(d[j], d[i] + R_transformed[i][j])

    for i in range(V):
        for j in range(V):
            if i == j:
                continue
            if d[j] > d[i] + R_transformed[i][j]:
                return True

    return False


'''Variation - arbitrage with transaction fee:

We might want to know if there is a loop 
where the product of the weights exceeds some
other value like 1.1.  So we will also be 
given an arbirary tolerance parameter as input.  

To make this a bit more involved we could also
ask to return the cycle if one exists.  
'''
